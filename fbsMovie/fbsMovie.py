# python $SIMS_MAF_DIR/examples/pythonScripts/opsimMovie.py enigma_1189_sqlite.db --sqlConstraint 'night=130' --outDir Output
#
# --ips = number of images to stitch together per second of view (default is 10).
# --fps = frames per second for the output video .. default just matches ips. If specified as higher than ips,
#         the additional frames will be copied to meet the fps requirement. If fps is lower than ips,
#         images will be removed from the sequence to maintain fps.
#         As a rule of thumb, fps>30 is undetectable to the human eye.
# --movieLength = can specify the length of the output video (in seconds), then automatically
#         calculate corresponding ips and fps based on the number of movie slices.
# --skipComp = skip computing the metrics and generating plots, just use files from disk.
#


import os, argparse
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import ticker
import colorcet as cc
import healpy as hp
from astropy.time import Time
import datetime
import pytz

import rubin_sim.maf as maf
from rubin_sim.utils import Site
from rubin_sim.utils import approx_altAz2RaDec

import warnings
import fnmatch


filter_rgb_map = {
    "u": (74 / 256, 125 / 256, 179 / 256),
    "g": (104 / 256, 173 / 256, 87 / 256),
    "r": (238 / 256, 134 / 256, 50 / 256),
    "i": (232 / 256, 135 / 256, 189 / 256),
    "z": (209 / 256, 53 / 256, 43 / 256),
    "y": (142 / 256, 82 / 256, 159 / 256),
}


def makeColorMap():
    filterColorMap = ListedColormap(list(filter_rgb_map.values()))
    return filterColorMap


def getData(opsDb, sqlconstraint):
    # Define columns we want from opsim database (for metrics, slicers and stacker info).
    colnames = [
        "observationStartMJD",
        "filter",
        "fieldRA",
        "fieldDec",
        "rotSkyPos",
        "observationStartLST",
        "moonRA",
        "moonDec",
        "moonPhase",
        "sunRA",
        "sunDec",
        "night",
    ]
    # Get data from database.
    simdata = opsDb.fetchMetricData(colnames, sqlconstraint)
    if len(simdata) == 0:
        raise Exception("No simdata found matching constraint %s" % (sqlconstraint))
    # Add stacker columns.
    filterIndxStacker = FilterIndxColorStacker()
    simdata = filterIndxStacker.run(simdata)
    return simdata


def setupMetrics(
    opsimName,
    metadata,
    constraint,
    plotlabel="",
    tNow=0,
    nightNow=0,
    tStep=40.0 / 24.0 / 60.0 / 60.0,
    years=0,
    onlyFilterColors=False,
    verbose=False,
):
    # Set up metrics and plotDicts (they will be bundled with the appropriate opsim slicers below).
    nvisitsMax = 90 * (years + 1)
    bundledict = {}
    figsize = (8, 6)
    s = maf.HealpixSlicer(nside=64)
    if not onlyFilterColors:
        m = maf.CountMetric("observationStartMJD", metricName="Nvisits")
        plotDict = {
            "colorMin": 0,
            "colorMax": nvisitsMax,
            "bgcolor": None,
            "fontsize": "large",
            "cmap": "cet_blues",
            "cbarOrientation": "vertical",
            "xlabel": "Number of visits",
            "title": "Cumulative visits (all bands)",
            "figsize": figsize,
        }
        bundledict["nvisits"] = maf.MetricBundle(
            m, s, constraint, runName=opsimName, plotDict=plotDict, metadata=metadata
        )
    m = FilterColorsMetric(tNow=tNow, nightNow=nightNow, tStep=tStep)
    plotDict = {
        "title": "%s" % (opsimName),
        "bgcolor": None,
        "figsize": figsize,
        "fontsize": "large",
    }
    bundledict["colors"] = maf.MetricBundle(
        m, s, constraint, runName=opsimName, plotDict=plotDict, metadata=metadata
    )
    if verbose:
        print("Set up metrics %f s" % (dt))
    return bundledict


def setupMovieSlicer(simdata, bins, verbose=False):
    movieslicer = maf.MovieSlicer(
        sliceColName="observationStartMJD", bins=bins, cumulative=True
    )
    movieslicer.setupSlicer(simdata)
    if verbose:
        print("Set up movie slicers in %f s" % (dt))
    return movieslicer


def runSlices(opsimName, metadata, simdata, bins, args, opsDb, verbose=False):
    # Set up the movie slicer.
    movieslicer = setupMovieSlicer(simdata, bins)
    # Set up formatting for output suffix.
    sliceformat = "%s0%dd" % ("%", int(np.log10(len(movieslicer))) + 1)

    lsst_site = Site("LSST")
    tz = pytz.timezone("Chile/Continental")

    filterColorMap = makeColorMap()
    # Run through the movie slicer slicePoints and generate plots at each point.
    for i, ms in enumerate(movieslicer):
        slicenumber = sliceformat % (i)
        if verbose:
            print(slicenumber)
        # Set up metrics.
        if args.movieStepsize != 0:
            tstep = args.movieStepsize
        else:
            tstep = ms["slicePoint"]["binRight"] - bins[i]
            if tstep > 1:
                tstep = 40.0 / 24.0 / 60.0 / 60.0
        # Identify the subset of simdata in the movieslicer 'data slice'
        subsetSdata = simdata[ms["idxs"]]
        visitNow = len(subsetSdata) - 1

        # Add simple view of time to plot label.
        # Assume the 'night' column is accurate to get time from start of survey in years/nights
        years = int(subsetSdata[visitNow]["night"] / 365)
        night = int(subsetSdata[visitNow]["night"] - years * 365)
        # And then calculate current local time for the hour
        time = Time(
            subsetSdata[visitNow]["observationStartMJD"], format="mjd", scale="utc"
        )
        td = time.to_datetime(tz)
        hour = td.hour
        minutes = td.minute
        plotlabel = f"Year {years:02d} Night {night:03d} Hour {hour:02d}:{minutes:02d}"

        # Set up metrics.
        constraint = ""
        bundledict = setupMetrics(
            opsimName,
            metadata,
            constraint,
            plotlabel=plotlabel,
            tNow=subsetSdata[visitNow]["observationStartMJD"],
            nightNow=subsetSdata[visitNow]["night"],
            tStep=tstep,
            years=years,
            verbose=verbose,
        )
        # clear out the stacker list because we ran them ourselves
        for mb in bundledict:
            bundledict[mb].stackerList = []
        # Set up metricBundleGroup to handle metrics calculation + plotting
        bg = maf.MetricBundleGroup(
            bundledict, opsDb, outDir=args.outDir, resultsDb=None, saveEarly=False
        )
        bg.runCurrent(constraint=constraint, simData=subsetSdata)

        # Plot data each metric, for this slice of the movie, adding slicenumber as a suffix for output plots.
        # Plotting here, rather than automatically via sliceMetric method because we're going to rotate the sky,
        #  and add extra legend info and figure text (for FilterColors metric).
        # ph = plots.PlotHandler(outDir=args.outDir, figformat='png', dpi=72, thumbnail=False, savefig=False)

        # lsst_site = Site('LSST')
        ecliptic_ra = np.arange(0, 360, 1)
        ecliptic_dec = np.sin(np.radians(ecliptic_ra)) * 23.5
        zenith_ra = subsetSdata[visitNow]["observationStartLST"]
        zenith_dec = lsst_site.latitude
        horizon_az = np.arange(0, 360, 1)
        horizon_alt = np.ones(len(horizon_az)) * 0  # 20
        horizon_ra, horizon_dec = approx_altAz2RaDec(
            horizon_alt,
            horizon_az,
            lsst_site.latitude,
            lsst_site.longitude,
            subsetSdata[visitNow]["observationStartMJD"],
        )
        moon_ra = subsetSdata[visitNow]["moonRA"]
        moon_dec = subsetSdata[visitNow]["moonDec"]
        moonPhase = subsetSdata[visitNow]["moonPhase"] / 100.0
        moon_alpha = np.max([moonPhase, 0.15])
        sun_ra = np.degrees(subsetSdata[visitNow]["sunRA"])
        sun_dec = np.degrees(subsetSdata[visitNow]["sunDec"])
        visit_ra = subsetSdata[visitNow]["fieldRA"]
        visit_dec = subsetSdata[visitNow]["fieldDec"]

        rot = (subsetSdata[visitNow]["observationStartLST"], 0, 0)
        # Create the plot for each metric and save it (after some additional manipulation).

        for mb in bundledict.values():
            if "visits" in mb.metric.name:
                fig = plt.figure(figsize=mb.plotDict["figsize"])
                rot = (subsetSdata[visitNow]["observationStartLST"], 0, 0)
                hp.mollview(
                    bundledict["nvisits"].metricValues,
                    min=mb.plotDict["colorMin"],
                    max=mb.plotDict["colorMax"],
                    badcolor="white",
                    fig=fig.number,
                    cmap=mb.plotDict["cmap"],
                    cbar=False,
                    flip="astro",
                    rot=rot,
                    title=mb.plotDict["title"],
                )
                hp.graticule(dpar=30, dmer=30, alpha=0.5)
                ll = hp.projscatter(
                    visit_ra,
                    visit_dec,
                    c="white",
                    marker="o",
                    alpha=0.5,
                    edgecolor="b",
                    lonlat=True,
                    s=70,
                )
                ll = hp.projplot(
                    horizon_ra,
                    horizon_dec,
                    color="k",
                    alpha=0.8,
                    lonlat=True,
                    label="Horizon",
                )
                ll = hp.projplot(
                    ecliptic_ra,
                    ecliptic_dec,
                    color="b",
                    alpha=0.5,
                    lonlat=True,
                    label="Ecliptic",
                )
                ll = hp.projscatter(
                    zenith_ra,
                    zenith_dec,
                    color="k",
                    marker="x",
                    lonlat=True,
                    label="Zenith",
                )
                ll = hp.projscatter(
                    sun_ra,
                    sun_dec,
                    color="white",
                    edgecolor="k",
                    marker="o",
                    s=50,
                    lonlat=True,
                    label="Sun",
                )
                ll = hp.projscatter(
                    moon_ra,
                    moon_dec,
                    color="k",
                    alpha=moon_alpha,
                    s=50,
                    lonlat=True,
                    marker="o",
                    label="\nMoon (Dark=Full)\n         (Light=New)",
                )
                # Add the time stamp info (plotlabel) with a fancybox.
                # plt.figtext(0.69, 0.95, '%s' % (plotlabel), fontsize='large',
                #            bbox=dict(boxstyle='Round, pad=0.7', fc='w', ec='k', alpha=0.5))
                # Make a color bar.
                ax = plt.gca()
                im = ax.get_images()[0]
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    cb = plt.colorbar(
                        im,
                        ax=ax,
                        shrink=0.5,
                        aspect=25,
                        pad=0.05,
                        location="bottom",
                        extendrect=True,
                    )
                    cb.set_label(mb.plotDict["xlabel"], fontsize="large")
                    tick_locator = ticker.MaxNLocator(nbins=10)
                    cb.locator = tick_locator
                    cb.update_ticks()

            elif "Color" in mb.metric.name and "_" not in mb.metric.name:
                fig = plt.figure(figsize=mb.plotDict["figsize"])
                hp.mollview(
                    bundledict["FilterColors_Color"].metricValues,
                    fig=fig.number,
                    min=0,
                    max=5,
                    alpha=bundledict["FilterColors_Alpha"].metricValues.filled(0),
                    cmap=filterColorMap,
                    cbar=False,
                    flip="astro",
                    rot=rot,
                    title=mb.plotDict["title"],
                )
                hp.graticule(dpar=30, dmer=30, alpha=0.5)
                ll = hp.projscatter(
                    visit_ra,
                    visit_dec,
                    c=[filter_rgb_map[subsetSdata[visitNow]["filter"]]],
                    marker="o",
                    alpha=1,
                    edgecolor="b",
                    lonlat=True,
                    s=70,
                )
                ll = hp.projplot(
                    horizon_ra,
                    horizon_dec,
                    color="k",
                    alpha=0.8,
                    lonlat=True,
                    label="Horizon",
                )
                ll = hp.projplot(
                    ecliptic_ra,
                    ecliptic_dec,
                    color="b",
                    alpha=0.5,
                    lonlat=True,
                    label="Ecliptic",
                )
                ll = hp.projscatter(
                    sun_ra,
                    sun_dec,
                    color="white",
                    edgecolor="k",
                    marker="o",
                    s=50,
                    lonlat=True,
                    label="Sun",
                )
                ll = hp.projscatter(
                    zenith_ra,
                    zenith_dec,
                    color="k",
                    marker="x",
                    lonlat=True,
                    label="Zenith",
                )
                ll = hp.projscatter(
                    moon_ra,
                    moon_dec,
                    color="k",
                    alpha=moon_alpha,
                    s=50,
                    lonlat=True,
                    marker="o",
                    label="\nMoon (Dark=Full)\n         (Light=New)",
                )
                plt.legend(
                    loc=(0.2, -0.24),
                    ncol=3,
                    frameon=False,
                    numpoints=1,
                    fontsize="large",
                    title_fontsize="large",
                )
                plt.figtext(
                    0.12,
                    0.13,
                    "Simulated survey pointings on the sky. One visit is ~40 seconds real-time.",
                    fontsize="large",
                )
                for i, f in enumerate(["u", "g", "r"]):
                    plt.figtext(
                        0.94,
                        0.3 - i * 0.04,
                        f,
                        fontsize="x-large",
                        fontweight="3",
                        horizontalalignment="center",
                        color=filter_rgb_map[f],
                    )
                for i, f in enumerate(["i", "z", "y"]):
                    plt.figtext(
                        0.94 + 0.03,
                        0.3 - i * 0.04,
                        f,
                        fontsize="x-large",
                        fontweight="3",
                        horizontalalignment="center",
                        color=filter_rgb_map[f],
                    )
                # Add the time stamp info (plotlabel) with a fancybox.
                plt.figtext(
                    0.68,
                    0.88,
                    "%s" % (plotlabel),
                    fontsize="large",
                    bbox=dict(boxstyle="Round, pad=0.3", fc="w", ec="k", alpha=0.5),
                )
            else:
                continue
            # Save figure.
            plt.savefig(
                os.path.join(
                    args.outDir, mb.metric.name + "_" + slicenumber + "_SkyMap.png"
                ),
                format="png",
                dpi=72 * 2,
            )
            plt.close("all")
            if verbose:
                print(
                    "Ran and plotted slice %s of movieslicer in %f s"
                    % (slicenumber, dt)
                )


def stitchMovie(bundledict, args):
    # Create a movie slicer to access the movie generation routine.
    movieslicer = maf.MovieSlicer()
    for b in bundledict.values():
        # Identify filenames.
        outfileroot = b.metric.name
        plotfiles = fnmatch.filter(
            os.listdir(args.outDir), outfileroot + "*_SkyMap.png"
        )
        slicenum = (
            plotfiles[0]
            .replace(outfileroot, "")
            .replace("_SkyMap.png", "")
            .replace("_", "")
        )
        sliceformat = "%s0%dd" % ("%", len(slicenum))
        n_images = len(plotfiles)
        if n_images == 0:
            raise Exception(
                "No images found in %s with name like %s" % (args.outDir, outfileroot)
            )
        # Set up ffmpeg parameters.
        # If a movieLength was specified... set args.ips/fps.
        if args.movieLength != 0.0:
            # calculate images/second rate
            args.ips = int(n_images / args.movieLength)
            print(
                "for a movie length of " + str(args.movieLength) + " IPS set to: ",
                args.ips,
            )
        if args.fps == 0:
            warnings.warn(
                "(FPS of 0) Setting fps equal to ips, up to a value of 30fps."
            )
            if args.ips <= 30:
                args.fps = args.ips
            else:
                args.fps = 30
        # Create the movie.
        movieslicer.makeMovie(
            outfileroot,
            sliceformat,
            plotType="SkyMap",
            figformat="png",
            outDir=args.outDir,
            ips=args.ips,
            fps=args.fps,
        )


if __name__ == "__main__":

    # Parse command line arguments for database connection info.
    parser = argparse.ArgumentParser()
    parser.add_argument("opsimDb", type=str, help="Opsim sqlite db file")
    parser.add_argument(
        "--dbDir",
        type=str,
        default=".",
        help="Directory containing opsim sqlite db file",
    )
    parser.add_argument(
        "--sqlConstraint",
        type=str,
        default=None,
        help="SQL constraint, such as filter='r' or night=1500. Default None.",
    )
    parser.add_argument(
        "--movieStepsize",
        type=float,
        default=0,
        help="Step size (in days) for movie slicer. " "Default sets 1 visit = 1 step.",
    )
    parser.add_argument(
        "--outDir", type=str, default="Output", help="Output directory."
    )
    parser.add_argument(
        "--addPreviousObs",
        action="store_true",
        default=False,
        help="Add all previous observations into movie (as background).",
    )
    parser.add_argument(
        "--skipComp",
        action="store_true",
        default=False,
        help="Just make movie from existing metric plot files.",
    )
    parser.add_argument(
        "--ips",
        type=float,
        default=30,
        help="The number of images per second in the movie. "
        "Will skip accordingly if fps is lower. Default 30.",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=30,
        help="The frames per second of the movie. Default 30.",
    )
    parser.add_argument(
        "--movieLength",
        type=float,
        default=0.0,
        help="Enter the desired length of the movie in seconds. "
        "If you do so, there is no need to enter images per second, it will be calculated.",
    )
    args = parser.parse_args()

    # cleaning up movie parameters
    if args.fps > 30:
        warnings.warn(
            "FPS above 30 reduces performance and is undetectable to the human eye. Try lowering the fps."
        )

    # Check if output directory exists; create if appropriate.
    if not os.path.isdir(args.outDir):
        if args.skipComp:
            raise Exception(
                "Skipping metric generation, expect to find plots in %s directory but it does not exist."
                % (args.outDir)
            )
        else:
            os.mkdir(args.outDir)

    # Check if user passed directory + filename as opsimDb.
    if len(os.path.dirname(args.opsimDb)) > 0:
        raise Exception(
            "OpsimDB should be just the filename of the sqlite file (not %s). Use --dbDir."
            % (args.opsimDb)
        )

    opsimName = args.opsimDb.replace("_sqlite.db", "")
    opsimName = opsimName.replace(".db", "")
    metadata = (
        args.sqlConstraint.replace("=", "")
        .replace("filter", "")
        .replace("'", "")
        .replace('"', "")
        .replace("/", ".")
    )

    if not args.skipComp:
        verbose = False
        # Get db connection info, and connect to database.
        dbfile = os.path.join(args.dbDir, args.opsimDb)
        oo = maf.OpsimDatabase(dbfile)
        sqlconstraint = args.sqlConstraint
        # Fetch the data from opsim.
        simdata = getData(oo, sqlconstraint)
        # Set up the time bins for the movie slicer.
        start_date = simdata["observationStartMJD"][0]
        if args.movieStepsize == 0:
            bins = simdata["observationStartMJD"]
        else:
            end_date = simdata["observationStartMJD"].max()
            bins = np.arange(
                start_date,
                end_date + args.movieStepSize / 2.0,
                args.movieStepSize,
                float,
            )
        if args.addPreviousObs:
            # Go back and grab all the data, including all previous observations.
            if "night =" in sqlconstraint:
                sqlconstraint = sqlconstraint.replace("night =", "night <=")
            elif "night=" in sqlconstraint:
                sqlconstraint = sqlconstraint.replace("night=", "night<=")
            simdata = getData(oo, sqlconstraint)
            # Update the first bin to be prior to the earliest opsim time.
            bins[0] = simdata["observationStartMJD"][0]

        # Run the movie slicer (and at each step, setup opsim slicer and calculate metrics).
        runSlices(opsimName, metadata, simdata, bins, args, oo, verbose=verbose)

    # Need to set up the metrics to get their names, but don't need to have realistic arguments.
    bundledict = setupMetrics(opsimName, metadata, args.sqlConstraint)
    stitchMovie(bundledict, args)
