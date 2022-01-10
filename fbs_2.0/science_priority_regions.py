# Dataset describing the regions of scientific priority for galactic science
# including both region location and area in galactic coordinates (described as
# numpy arrays named *_region_pix) as well as estimated weightings of the
# relative priorities/required frequency of observations in the different
# filters (dictionaries named as filterset_*)
#
# These regions were proposed in the Rubin Cadence White Papers (2018) as
# referenced in the papers described below, which can be found at:
# https://www.lsst.org/submitted-whitepaper-2018
import numpy as np
from astropy import units as u
from astropy.coordinates import Galactic, SkyCoord
from gc_all_lsst_field import fetch_GlobularClusters_in_LSST_footprint

__all__ = ['fetch_priority_region_data', 'bono_survey_regions', 'load_SFR', 'calc_hp_pixels_for_region']

def fetch_priority_region_data(ahp):
    """Function returns the specified HEALpix regions and filter preferences
    for survey regions of interest to galactic science.
    Parameter ahp is required to be a HEALpix object.
    """

    # Galactic Plane survey regions
    # A number of papers described overlapping regions with the following areas:
    # Street: griz, cadence 2-3d , -85.0 < l <+85.0◦, -10.0 < b <+10.0◦
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30499/street_wide_area_gal_plane_survey.pdf
    # Gonzales survey 1: i, N visits over 10yrs
    # Gonzales survey 2: grizy, Year 1 only
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30589/gonzalez_stellarpops_gp.pdf
    # Bono shallow: ugrizy 2-3d cadence (WFD)
    # Bono deep: izy, 2-3d cadence (WFD)
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30571/dalla_ora_vestale_gp.pdf
    # Straeder: ugrizy 2-3d cadence or rolling
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30482/strader_plane_wfd.pdf
    filterset_gp = { 'u': 0.05, 'g': 0.225, 'r': 0.225, 'i': 0.225, 'z': 0.225, 'y': 0.05 }
    gp_region_pix1 = calc_hp_pixels_for_region(43.5, 0.0, 90.0, 20.0, 500, ahp)
    gp_region_pix2 = calc_hp_pixels_for_region(317.5, 0.0, 90.0, 20.0, 500, ahp)
    gp_region_pix = np.concatenate((gp_region_pix1.flatten(),gp_region_pix2.flatten()))

    filterset_Gonzalez_gp = { 'u': 0.0, 'g': 0.0, 'r': 0.0, 'i': 1.0, 'z': 0.0, 'y': 0.0 }
    gp_region_pix1 = calc_hp_pixels_for_region(7.5, 0.0, 15.0, 20.0, 500, ahp)
    gp_region_pix2 = calc_hp_pixels_for_region(352.5, 0.0, 15.0, 20.0, 500, ahp)
    Gonzalez_gp_pix = np.concatenate((gp_region_pix1.flatten(),gp_region_pix2.flatten()))

    (Bono_shallow_pix, Bono_deep_pix) = bono_survey_regions(ahp)
    filterset_Bono_shallow = { 'u': 0.1, 'g': 0.1, 'r': 0.2, 'i': 0.2, 'z': 0.2, 'y': 0.2 }
    filterset_Bono_deep = { 'u': 0.0, 'g': 0.0, 'r': 0.0, 'i': 0.4, 'z': 0.3, 'y': 0.3 }

    filterset_Bonito_gp = { 'u': 0.0, 'g': 0.3, 'r': 0.4, 'i': 0.3, 'z': 0.0, 'y': 0.0 }
    gp_region_pix1 = calc_hp_pixels_for_region(43.5, 0.0, 90.0, 5.0, 500, ahp)
    gp_region_pix2 = calc_hp_pixels_for_region(317.5, 0.0, 90.0, 5.0, 500, ahp)
    Bonito_gp_pix = np.concatenate((gp_region_pix1.flatten(),gp_region_pix2.flatten()))

    # Magellenic Clouds regions
    # Poleski: gri, <1d cadence
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30584/poleski_smc_mini.pdf
    # Street: griz, 2-3d cadence
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30499/street_wide_area_gal_plane_survey.pdf
    # Clementini: gri, WFD cadence
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30585/clementini_stellarpop_wfd.pdf
    # Olsen: ugrizy, WFD, logarithmic spacing
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30645/olsen_mc_mini.pdf
    # LMC  277.77 - 283.155, -35.17815 - -30.59865
    filterset_LMC = { 'u': 0.0, 'g': 0.2, 'r': 0.2, 'i': 0.2, 'z': 0.2, 'y': 0.1 }
    LMC_pix = calc_hp_pixels_for_region(280.4652, -32.888443, (322.827/60), (274.770/60), 100, ahp)

    # SMC 301.4908 - 304.126, -45.1036 - -43.5518
    filterset_SMC = { 'u': 0.0, 'g': 0.2, 'r': 0.2, 'i': 0.2, 'z': 0.2, 'y': 0.1 }
    SMC_pix = calc_hp_pixels_for_region(302.8084, -44.3277, (158.113/60), (93.105/60), 100, ahp)

    # Galactic Bulge regions
    # Street: griz, simultaneous with Rubin + 3d cadence in same years
    # https://arxiv.org/pdf/1812.04445.pdf
    # Straeder: ugrizy 2-3d cadence or rolling
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30482/strader_plane_wfd.pdf
    # Bono shallow: ugrizy 2-3d cadence (WFD)
    # Bono deep: izy, 2-3d cadence (WFD)
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30571/dalla_ora_vestale_gp.pdf
    filterset_bulge = { 'u': 0.1, 'g': 0.2, 'r': 0.3, 'i': 0.3, 'z': 0.2, 'y': 0.2 }
    bulge_pix = calc_hp_pixels_for_region(2.216, -3.14, 3.5, 3.5, 50, ahp)

    # Resolved stellar population regions
    # Clementini survey, gri, WFD cadence
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30585/clementini_stellarpop_wfd.pdf
    filterset_Clementini = { 'u': 0.0, 'g': 0.3, 'r': 0.4, 'i': 0.3, 'z': 0.0, 'y': 0.0 }
    M54_pix = calc_hp_pixels_for_region(5.60703,-14.08715, 3.5, 3.5, 20, ahp)
    Sculptor_pix = calc_hp_pixels_for_region(287.5334, -83.1568, 3.5, 3.5, 20, ahp)
    Carina_pix = calc_hp_pixels_for_region(260.1124, -22.2235, 3.5, 3.5, 20, ahp)
    Fornax_pix = calc_hp_pixels_for_region(237.1038, -65.6515, 3.5, 3.5, 20, ahp)
    Phoenix_pix = calc_hp_pixels_for_region(272.1591, -68.9494, 3.5, 3.5, 20, ahp)
    Antlia2_pix = calc_hp_pixels_for_region(264.8955, 11.2479, 3.5, 3.5, 20, ahp)
    Clementini_regions = np.concatenate((M54_pix.flatten(), Sculptor_pix.flatten()))
    for cluster in [Carina_pix, Fornax_pix, Phoenix_pix, Antlia2_pix]:
        Clementini_regions = np.concatenate((Clementini_regions, cluster.flatten()))

    # Bonito survey regions
    # ugrizy in WFD plus additional gri every 30min, 10hrs/night for 7 nights.
    # https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-30505/bonito_carina_dd.pdf
    filterset_Bonito = { 'u': 0.1, 'g': 0.1, 'r': 0.1, 'i': 0.1, 'z': 0.1, 'y': 0.1 }
    EtaCarina_pix = calc_hp_pixels_for_region(287.5967884538, -0.6295111793, 3.5, 3.5, 20, ahp)
    OrionNebula_pix = calc_hp_pixels_for_region(209.0137, -19.3816, 3.5, 3.5, 20, ahp)
    NGC2264_pix = calc_hp_pixels_for_region(202.9358, 2.1957, 3.5, 3.5, 20, ahp)
    NGC6530_pix = calc_hp_pixels_for_region(6.0828, -01.3313, 3.5, 3.5, 20, ahp)
    NGC6611_pix = calc_hp_pixels_for_region(16.9540, 0.7934, 3.5, 3.5, 20, ahp)
    Bonito_regions = np.concatenate((EtaCarina_pix.flatten(), OrionNebula_pix.flatten()))
    for cluster in [NGC2264_pix, NGC6530_pix, NGC6611_pix]:
        Bonito_regions = np.concatenate((Bonito_regions, cluster.flatten()))

    # Globular clusters
    # ee module gc_all_lsst_field.py
    filterset_gc = { 'u': 0.0, 'g': 0.2, 'r': 0.3, 'i': 0.3, 'z': 0.2, 'y': 0.0 }
    gc_list = fetch_GlobularClusters_in_LSST_footprint()
    cluster0_pix = calc_hp_pixels_for_region(gc_list[0]['l'], gc_list[0]['b'], 3.5, 3.5, 20, ahp)
    cluster1_pix = calc_hp_pixels_for_region(gc_list[1]['l'], gc_list[1]['b'], 3.5, 3.5, 20, ahp)
    gc_regions = np.concatenate((cluster0_pix.flatten(), cluster1_pix.flatten()))
    for cluster in gc_list[2:]:
        cluster0_pix = calc_hp_pixels_for_region(cluster['l'], cluster['b'], 3.5, 3.5, 20, ahp)
        gc_regions = np.concatenate((gc_regions, cluster0_pix.flatten()))

    # Star Forming Regions:
    filterset_sfr = { 'u': 0.1, 'g': 0.1, 'r': 0.1, 'i': 0.1, 'z': 0.1, 'y': 0.1 }
    SFR_list = load_SFR()
    sfr0_pix = calc_hp_pixels_for_region(SFR_list[0]['l'], SFR_list[0]['b'], 3.5, 3.5, 20, ahp)
    sfr1_pix = calc_hp_pixels_for_region(SFR_list[1]['l'], SFR_list[1]['b'], 3.5, 3.5, 20, ahp)
    sfr_regions = np.concatenate((sfr0_pix.flatten(), sfr1_pix.flatten()))

    for sfr in SFR_list[2:]:
        sfr0_pix = calc_hp_pixels_for_region(sfr['l'], sfr['b'], 3.5, 3.5, 20, ahp)
        sfr_regions = np.concatenate((sfr_regions, sfr1_pix.flatten()))

    # Dictionaries combining the data for the region HEALpix specifications.
    # Note: Bonito regions removed from these lists after consultation with
    # authors of the White Paper, which refers to a more specialised strategy
    high_priority_regions = {'Galactic_Plane': {'pixel_region': gp_region_pix,
                                                'filterset': filterset_gp},
                             'Gonzalez_Plane_region': {'pixel_region': Gonzalez_gp_pix,
                                                       'filterset': filterset_Gonzalez_gp},
                             'Bonito_Plane_region': {'pixel_region': Bonito_gp_pix,
                                                     'filterset': filterset_Bonito_gp},
                             'Bono_shallow_survey': {'pixel_region': Bono_shallow_pix,
                                                     'filterset': filterset_Bono_shallow},
                             'Bono_deep_survey': {'pixel_region': Bono_deep_pix,
                                                  'filterset': filterset_Bono_deep},
                             'Large_Magellenic_Cloud': {'pixel_region': LMC_pix,
                                                        'filterset': filterset_LMC},
                             'Small_Magellenic_Cloud': {'pixel_region': SMC_pix,
                                                        'filterset': filterset_SMC},
                             'Galactic_Bulge': {'pixel_region': bulge_pix,
                                                'filterset': filterset_bulge},
                             'Clementini_regions': {'pixel_region': Clementini_regions,
                                                    'filterset': filterset_Clementini},
                             'Globular_Clusters': {'pixel_region': gc_regions,
                                                   'filterset': filterset_gc},
                             'SFR': {'pixel_region': sfr_regions,
                                     'filterset': filterset_sfr} }
                            # 'Bonito_regions': Bonito_regions}
    regions_outside_plane = {'LMC': {'pixel_region': LMC_pix, 'filterset': filterset_LMC},
                             'SMC': {'pixel_region': SMC_pix, 'filterset': filterset_SMC},
                             'Clementini': {'pixel_region': Clementini_regions, 'filterset': filterset_Clementini},
                             # 'Bonito': {'pixel_region': Bonito_regions, 'filterset': filterset_Bonito},
                             'Globular_Clusters': {'pixel_region': gc_regions, 'filterset': filterset_gc},
                             'SFR': {'pixel_region': sfr_regions, 'filterset': filterset_sfr},
                             }

    return high_priority_regions, regions_outside_plane

def bono_survey_regions(ahp):

    n_points = 500
    l = np.linspace(-20.0, 20.0, n_points) * u.deg
    b = np.linspace(-15.0, 10.0, n_points) * u.deg
    LL,BB = np.meshgrid(l, b)
    coords = SkyCoord(LL, BB, frame=Galactic())
    shallow_pix = ahp.skycoord_to_healpix(coords)


    n_points = 100
    l = np.linspace(-20.0, 20.0, n_points) * u.deg
    b = np.linspace(-3.0, 3.0, n_points) * u.deg
    LL,BB = np.meshgrid(l, b)
    coords = SkyCoord(LL, BB, frame=Galactic())
    deep_pix = ahp.skycoord_to_healpix(coords)

    return shallow_pix, deep_pix

def load_SFR():
    data_file = 'Handbook_Distances_Zucker2020.dat'
    f = open(data_file, 'r')
    file_lines = f.readlines()
    f.close()

    SFR_list = []
    for line in file_lines:
        if 'name l b' not in line:
            entries = line.replace('\n','').split()
            sfr = {'name': entries[0], 'l': float(entries[1]), 'b': float(entries[2])}
            SFR_list.append(sfr)

    return SFR_list

def calc_hp_pixels_for_region(l_center, b_center, l_width, b_height, n_points, ahp):

    halfwidth_l = l_width / 2.0
    halfheight_b = b_height / 2.0

    l_min = max( (l_center-halfwidth_l), 0 )
    l_max = min( (l_center+halfwidth_l), 360.0 )
    b_min = max( (b_center-halfheight_b), -90.0 )
    b_max = min( (b_center+halfheight_b), 90.0 )

    l = np.linspace(l_min, l_max, n_points) * u.deg
    b = np.linspace(b_min, b_max, n_points) * u.deg

    LL,BB = np.meshgrid(l, b)

    coords = SkyCoord(LL, BB, frame=Galactic())

    pixels = ahp.skycoord_to_healpix(coords)

    return pixels
