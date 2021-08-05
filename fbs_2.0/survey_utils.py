import warnings
import numpy as np
import numpy.ma as ma
import healpy as hp
import rubin_sim.maf as maf

__all__ = ['scalingfunc', 'calc_area_time', 'average_ra_window', 'plot_sky', 'plot_footprints']

def scalingfunc(survey_frac=None, nvisits_per_pointing=None, area=None):
    # How much survey time .. approximately .. is it likely to take to cover a given area?
    # We can use a rough scaling derived from
    # https://github.com/lsst-pst/survey_strategy/blob/master/fbs_1.7/SurveyFootprints-NvisitsVsArea.ipynb
    # x = (scale['NvisitPerPoint*']/825) * (scale['Area']/18000) / (scale['t']/0.77)  == constant (~1)
    defaults = {'survey_frac': 0.77, 'area': 18000, 'nvisits_per_pointing': 825}
    if area is None:
        area = (survey_frac / defaults['survey_frac']) / \
               (nvisits_per_pointing / defaults['nvisits_per_pointing'])
        return area * defaults['area']
    elif nvisits_per_pointing is None:
        nvisits_per_pointing = (survey_frac / defaults['survey_frac']) / (area / defaults['area'])
        return nvisits_per_pointing * defaults['nvisits_per_pointing']
    elif survey_frac is None:
        survey_frac = nvisits_per_pointing / defaults['nvisits_per_pointing'] * area / defaults['area']
        return survey_frac * defaults['survey_frac']

def calc_area_time(footprint, nvis_peak=825, nside=64, verbose=False):
    # Given a survey footprint, returns (effective) area in footprint and fraction of survey time required
    eff_area = footprint.sum() * hp.nside2pixarea(nside, degrees=True)
    nvis_srd_min = 750 * 1.08
    srd_area = (footprint[np.where(footprint * nvis_peak > nvis_srd_min)].sum()
                * hp.nside2pixarea(nside, degrees=True))
    # survey time required?
    time = scalingfunc(nvisits_per_pointing=nvis_peak, area=eff_area)
    if (verbose):
        print(f'Effective area in footprint {eff_area}')
        print(f'Area in footprint which can contribute to SRD {srd_area}')
        print(f'Approximate fraction of survey time required for footprint {time}')
    return eff_area, srd_area, time

def average_ra_window(skyarea, haRange=3):
    ha_limit = haRange * 15
    step = 3
    ra = np.arange(0, 360  + step/2, step)
    area = np.zeros(len(ra), float)
    for i, ra_cen in enumerate(ra):
        # consider wrap-around at RA=0, but calculate a running window's width of 'area'
        # this is the area available within ha_limit when a given RA is overhead
        window = np.where((np.abs(skyarea.ra - ra_cen) < ha_limit) |
                          (np.abs(skyarea.ra - ra_cen) > 360 - ha_limit), 1, 0)
        area[i] = skyarea.total[np.where(window == 1)].sum() * hp.nside2pixarea(skyarea.nside, degrees=True)
    return ra, area

def plot_sky(skymap, plotDict=None, slicer=maf.HealpixSlicer(64), maskBelow=0, lamb=False):
    # This just makes it easier to make sure these footprint maps match MAF
    plotFunc = maf.HealpixSkyMap()
    if lamb:
        plotFunc.healpy_visufunc = hp.azeqview
        plotFunc.healpy_visufunc_params['lamb'] = True
        plotFunc.healpy_visufunc_params['rot'] = (0, -90, 0)
        plotFunc.healpy_visufunc_params['reso'] = 18
    t = ma.MaskedArray(data=np.array(skymap, float), mask=np.where(skymap > maskBelow, 0, 1))
    if plotDict is None:
        # Just because of how the slicer works, this cannot be None
        plotDict = {'colorMin': None}
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        plotFunc(t, slicer, plotDict)

def plot_footprints(sky):
    colorMax = np.percentile(sky.total, 98) * 1.2
    plot_sky(sky.total, plotDict={'title':  'All filters', 'colorMax': colorMax, 'figsize': (8, 6)})
    for f in sky.filterlist:
        colorMax = np.percentile(sky.total_perfilter[f], 98) * 1.2
        plot_sky(sky.total_perfilter[f], plotDict={'title': f'Filter {f}',
                                                   'colorMax': colorMax, 'figsize': (8, 6)})