import os, argparse
import warnings
import fnmatch
import time

import numpy as np
import matplotlib
matplotlib.use('Agg')

import rubin_sim.maf as maf


def dtime(time_prev):
   return (time.time() - time_prev, time.time())

def get_benchmarks(filtername, cumulative):
    if cumulative:
        runLength=10
    if not cumulative:
        runLength = 1
    benchmarkVals = maf.scale_benchmarks(runLength, benchmark="design")
    benchmarkVals["coaddedDepth"] = maf.calc_coadded_depth(
        benchmarkVals["nvisits"], benchmarkVals["singleVisitDepth"]
    )
    nvisitsMin = 0
    if filtername is None or filtername == "all":
        nvisitsMax = np.array(list(benchmarkVals['nvisits'].values())).sum() * 1.2
    else:
        nvisitsMax = benchmarkVals['nvisits'][filtername] * 1.2
    nvisitsMax = int(np.ceil(nvisitsMax * 10) / 10)

    if filtername is None or filtername == "all":
        coaddMin = None
        coaddMax = None
    else:
        coaddMin = round(benchmarkVals['coaddedDepth'][filtername], 1) - 1.5
        coaddMax = round(benchmarkVals['coaddedDepth'][filtername], 1) + 1

    return nvisitsMin, nvisitsMax, coaddMin, coaddMax

def setupMetrics(opsimName, metadata,  plotlabel=None, cumulative=False,
                 filtername=None, verbose=False):
    """
    Define and instantiate metrics.
    """
    # Define and set up metrics.
    # Note that it is useful to set up the plotDict so that the min/max range for the plot
    #  is the same for all movie frames.
    if plotlabel is None:
        plotlabel = ''
    t = time.time()
    metricList = []
    plotDictList = []
    # Simple metrics: coadded depth and number of visits
    # Modify metrics here and it should propagate elsewhere (as needed) automatically
    nvisitsMin, nvisitsMax, coaddMin, coaddMax = get_benchmarks(filtername, cumulative)

    figsize = (8, 8)
    title = 'Simulation %s: %s' % (opsimName, metadata)

    if coaddMin is not None:
        metricList.append(maf.Coaddm5Metric('fiveSigmaDepth', metric_name='Coaddm5'))
        plotDictList.append({'color_min': coaddMin, 'color_max': coaddMax,
                             'label': plotlabel, 'title': title, 'figsize': figsize})

    metricList.append(maf.CountMetric('observationStartMJD', metric_name='NVisits'))
    plotDictList.append({'color_min': nvisitsMin, 'color_max': nvisitsMax,
                         'cbar_format': '%d',
                          'label': plotlabel, 'title': title + 'NVisits', 'figsize': figsize})
    dt, t = dtime(t)
    if verbose:
        print('Set up metrics %f s' % (dt))
    return metricList, plotDictList

def setupHealpixSlicer(args, verbose=False):
    """
    Instantiates and sets up the healpix slicer, using the subset of simdata (simdatasubset)
    which should be used for this slice of the movieslicer.
    raCol and decCol identify the columns to be used by the healpix slicer.
    nside sets the resolution of the healpix slicer.
    Returns the healpix slicer.
    """
    t = time.time()
    hs = maf.HealpixSlicer(nside=args.nside, lon_col=args.raCol, lat_col=args.decCol)
    dt, t = dtime(t)
    if verbose:
        print('Set up healpix slicer %f s' %(dt))
    return hs

def setupMovieSlicer(simdata, binsize = 365.0, cumulative=True, verbose=False):
    """
    Instantiates and sets up the MovieSlicer.
    Uses simdata (all the opsim data) and binsize to set the bin sizes.
    Uses 'cumulative' to determine whether slicer should be cumulative or binned.
    Returns the movie slicer.
    """
    t = time.time()
    ms = maf.MovieSlicer(slice_col_name='observationStartMJD', bin_size=binsize, cumulative=cumulative)
    ms.setup_slicer(simdata)
    dt, t = dtime(t)
    if verbose:
        print('Set up movie slicer in %f s' %(dt))
    return ms


def runSlices(opsimName, metricList, plotDictList, metadata, simdata, bins, args, filtername=None, verbose=False):
    """
    Set up and run the movie slicer, and at each step,
    setup the healpix slicer and run the metrics, creating and saving the plots.
    """
    # Set up movie slicer
    movieslicer = setupMovieSlicer(simdata, binsize = args.movieStepsize, cumulative=args.cumulative)
    start_date = movieslicer[0]['slice_point']['bin_left']
    sliceformat = '%s0%dd' %('%', int(np.log10(len(movieslicer)))+1)
    # Run through the movie slicer slicePoints:
    for i, movieslice in enumerate(movieslicer):
        t = time.time()
        slicenumber = sliceformat %(i)
        """
        # Set up plot label.
        timeInterval = '%.2f to %.2f' %(movieslice['slicePoint']['binLeft']-start_date,
                                        movieslice['slicePoint']['binRight']-start_date)
        """
        # Or add simple view of time to plot label.
        times_from_start = movieslice['slice_point']['bin_right'] - (int(bins[0]) + 0.16 - 0.5)
        # Opsim years are 365 days (not 365.25)
        years = int(times_from_start/365)
        days = times_from_start - years*365
        plotlabel = 'Year %d Day %.4f' %(years, days)

        # Identify the subset of simdata in the movieslicer 'data slice'
        simdatasubset = simdata[movieslice['idxs']]

        # Set up healpix slicer on subset of simdata provided by movieslicer
        hs = setupHealpixSlicer(args)

        bundles = []

        for metric, plotDict in zip(metricList, plotDictList):
            bundles.append(maf.MetricBundle(metric, hs, constraint=args.sqlConstraint,
                                           info_label=metadata, run_name=opsimName, plot_dict=plotDict,
                                           plot_funcs=[maf.HealpixSkyMap()]))
        # Remove (default) stackers from bundles, because we've already run them above on the original data.
        for mb in bundles:
            mb.stackerList = []
        bundledict = maf.make_bundles_dict_from_list(bundles)
        # Set up metricBundleGroup to handle metrics calculation + plotting
        bg = maf.MetricBundleGroup(bundledict, args.opsimDb, out_dir=args.outDir, results_db=None, save_early=False)
        # Calculate metric data values for simdatasubset (this also sets up indexing in the slicer)
        bg.set_current(args.sqlConstraint)
        bg.run_current(constraint=args.sqlConstraint, sim_data=simdatasubset)
        # Plot data for this slice of the movie, adding slicenumber as a suffix for output plots
        bg.plot_all(outfile_suffix=slicenumber, closefigs=True, dpi=72, thumbnail=False, fig_format='png')
        # Write the data -- uncomment if you want to do this.
        # sm.writeAll(outfileSuffix=slicenumber)
        if verbose:
            dt, t = dtime(t)
            print('Ran and plotted slice %s of movieslicer in %f s' %(slicenumber, dt))


def stitchMovie(metricList, metadata, args):
    """
    Create a movie for each metric from the plots generated in runSlices.
    Uses metricList to identify which metrics should be used as input for movies.
    Uses args to identify framerates for the movie slicer.
    """
    # Create a movie slicer to access the movie generation routine.
    movieslicer = maf.MovieSlicer()
    # Identify roots of distinct output plot files.
    outfileroots = []
    for metric in metricList:
        mName = metric.name.replace('  ', ' ').replace(' ', '_').replace('.', '_').replace(',', '')
        dbName = args.opsimDb.replace('_sqlite.db', '')
        dbName = dbName.replace('.db', '')
        if metadata != '':
            outfileroots.append('_'.join([dbName, mName, metadata, 'HEAL']))
        else:
            outfileroots.append('_'.join([dbName, mName, 'HEAL']))
    outfileroots = [o.replace('.', '_') for o in outfileroots]

    for outfileroot in outfileroots:
        # Identify filenames.
        plotfiles = fnmatch.filter(os.listdir(args.outDir), outfileroot + "*SkyMap.png")
        if len(plotfiles) == 0:
            print(f"Couldn't find files containing {outfileroot}")
        slicenum = plotfiles[0].replace(outfileroot, '').replace('_SkyMap.png', '').replace('_', '')
        sliceformat = '%s0%dd' %('%', len(slicenum))
        n_images = len(plotfiles)
        if n_images == 0:
            raise Exception('No images found in %s with name like %s' %(args.outDir, outfileroot))
        # Set up ffmpeg FPS/IPS parameters.
        # If a movieLength was specified... set args.ips/fps according to the number of images.
        if args.movieLength != 0.0:
            #calculate images/second rate
            args.ips = n_images/float(args.movieLength)
            print("For a movie length of " + str(args.movieLength) + " IPS set to: ", args.ips)
        if args.fps == 0.0:
            warnings.warn('(FPS of 0.0) Setting fps equal to ips, up to a value of 30fps.')
            if args.ips <= 30.0:
                args.fps = args.ips
            else:
                args.fps = 30.0
        if args.fps < args.ips:
            warnings.warn('Will create movie, but FPS < IPS, so some frames may be skipped.')
        if args.fps > 30.0:
            warnings.warn('Will create movie, but FPS above 30 reduces performance '
                          'and is undetectable to the human eye.')
        # Create the movie.
        movieslicer.make_movie(outfileroot, sliceformat, plot_type='SkyMap', fig_format='png',
                                out_dir=args.outDir, ips=args.ips, fps=args.fps)


if __name__ == '__main__':

    # Parse command line arguments for database connection info.
    parser = argparse.ArgumentParser()
    parser.add_argument("opsimDb", type=str, help="Opsim sqlite db file")
    parser.add_argument("--skipComp", action = 'store_true', default=False,
                        help="Just make movie from existing metric plot files.")
    parser.add_argument("--sqlConstraint", type=str, default="filter='r'",
                        help="SQL constraint, such as filter='r' or propID=182")
    parser.add_argument("--movieStepsize", type=float, default=365.,
                        help="Step size for movie slicer. Default 365 (1 year).")
    parser.add_argument("--nside", type=int, default=128,
                        help="NSIDE parameter for healpix grid resolution. Default 128.")
    parser.add_argument("--raCol", type=str, default='fieldRA',
                        help="Name of RA column (fieldRA / nondithered is default).")
    parser.add_argument("--decCol", type=str, default='fieldDec',
                        help="Name of Dec column (fieldDec / nondithered is default).")
    parser.add_argument("--binned", action = 'store_true', default=False, help="Create binned, non-cumulative movie.")
    parser.add_argument("--outDir", type=str, default=None, help="Output directory.")
    parser.add_argument("--ips", type=float, default = 10.0,
                        help="The number of images per second in the movie. "
                             "Will skip accordingly if fps is lower (set this first).")
    parser.add_argument("--fps", type=float, default = 0.0, help="The frames per second of the movie (can be set from ips).")
    parser.add_argument("--movieLength", type=float, default=0.0,
                        help="Enter the desired length of the movie in seconds. "
                             "If done, then no need to enter images per second as it will be calculated.")

    args = parser.parse_args()

    # Flip the flag to the more intuitive value within the code. However, we anticipate most movies will be cumulative,
    #  so the flag is flipped in the argument list.
    args.cumulative = not args.binned

    start_t = time.time()

    opsimName = os.path.split(args.opsimDb)[-1].replace('.db', '')
    sqlconstraint = args.sqlConstraint
    if 'filter' in sqlconstraint:
        filtername = sqlconstraint.split('filter')[-1].replace('=', '')
        filtername = filtername.replace('"', '').replace("'", '').lstrip(' ')[0]
    else:
        filtername = "all"
    metadata = sqlconstraint.replace('=', '').replace('filter', '').replace("'", '') \
        .replace('"', '').replace('/', '.')

    if args.outDir is None:
        args.outDir = opsimName
    # Check if directory exists; create if appropriate.
    if not os.path.isdir(args.outDir):
        if args.skipComp:
            raise Exception('Skipping metric generation, expect to find plots in %s directory but it does not exist.'
                            %(args.outDir))
        else:
            os.mkdir(args.outDir)

    # Define metrics, stackers and slicer so that we can see what columns we need from database.
    metricList, plotDictList = setupMetrics(opsimName, metadata,
                                            cumulative=args.cumulative,
                                            filtername=filtername)
    # Define the slicer to be used at each step of the movie slicer.
    subslicer = setupHealpixSlicer(args)

    if not args.skipComp:
        # Get data from database.
        dbcols = ['observationStartMJD', 'fiveSigmaDepth', args.raCol, args.decCol, 'rotSkyPos']
        simdata = maf.get_sim_data(args.opsimDb, sqlconstraint, dbcols)
        # Generate the bins for the movie slicer.
        start_date = simdata['observationStartMJD'].min()
        end_date = simdata['observationStartMJD'].max()
        bins = np.arange(start_date, end_date+args.movieStepsize/2.0, args.movieStepsize, float)
        # Run the movie slicer (and at each step, healpix slicer and calculate metrics).
        gm = runSlices(opsimName, metricList, plotDictList, metadata, simdata, bins, args)

    # Build movie.
    stitchMovie(metricList, metadata, args)

    end_t, start_t = dtime(start_t)
    print('Total time: ', end_t)
