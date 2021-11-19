import os
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
from astropy_healpix import HEALPix
from astropy.coordinates import TETE
from science_priority_regions import fetch_priority_region_data

# Configuration
STAR_MAP_DIR = './star_density_maps'
STAR_MAP_FILE = 'TRIstarDensity_r_nside_64.npz'
OUTPUT_DIR = './footprint_maps'
# Note if NSIDE is changed, a corresponding map of star density data must be used
NSIDE = 64
# Plotting scale range:
plot_min = 0.598
plot_max = 7.545

__all__ = ['generate_gp_maps']

# This seems to ONLY work properly if nside=64 .. why?
def generate_gp_maps(nside=NSIDE):

    npix = hp.nside2npix(nside)

    # Do some juggling to see if we can just use the rubin_sim data maps
    mapDir = os.getenv('RUBIN_SIM_DATA')
    if mapDir is None:
        mapDir = os.path.join(os.getenv('HOME'), 'rubin_sim_data')
    mapDir = os.path.join(mapDir, 'maps', 'TriMaps')
    if not os.path.isdir(mapDir):
        mapDir = STAR_MAP_DIR

    (ahp, hp_log_star_density) = create_star_density_map(mapDir, nside)

    (high_priority_regions, regions_outside_plane) = fetch_priority_region_data(ahp)

    vote_maps = build_priority_map(high_priority_regions, regions_outside_plane,
                                hp_log_star_density, npix)
    return vote_maps

def create_star_density_map(mapDir = STAR_MAP_DIR, nside=NSIDE):
    """Function to create a HEALPix object based on a map of Milky Way stellar
    density generated from the Trilegal galactic model.  These data are in
    Galactic coordinates, so this needs to be rotated in order to map it
    to healpix"""

    star_density_map = load_star_density_data(mapDir=mapDir, nside=nside, limiting_mag=24.7)
    hp_star_density = rotateHealpix(star_density_map)
    hp_log_star_density = np.log10(hp_star_density)

    ahp = HEALPix(nside=nside, order='ring', frame=TETE())

    return ahp, hp_log_star_density

def load_star_density_data(mapDir=STAR_MAP_DIR, nside=NSIDE, limiting_mag=28.0):

    star_map_file = f'TRIstarDensity_r_nside_{nside :d}.npz'
    data_file = os.path.join(mapDir, star_map_file)
    if os.path.isfile(data_file):
        npz_file = np.load(data_file)
        with np.load(data_file) as npz_file:
            star_map = npz_file['starDensity']
            mag_bins = npz_file['bins']

            dmag = abs(mag_bins - limiting_mag)
            idx = np.where(dmag == dmag.min())[0]

            star_density_map = np.copy(star_map[:,idx]).flatten()
            star_density_map = hp.reorder(star_density_map, n2r=True)

        return star_density_map

    else:
        raise IOError('Cannot find star density map data file at '+data_file)

    return None

def rotateHealpix(hpmap, transf=['C','G'], phideg=0., thetadeg=0.):
    """Rotates healpix map from one system to the other. Returns reordered healpy map.
    Healpy coord transformations are used, or you can specify your own angles in degrees.
    To specify your own angles, ensure that transf has length != 2.
    Original code by Xiaolong Li
    """

    # For reasons I don't understand, entering in ['C', 'G'] seems to do the
    # transformation FROM galactic TO equatorial. Possibly something buried in
    # the conventions used by healpy.

    # Heavily influenced by stack overflow solution here:
    # https://stackoverflow.com/questions/24636372/apply-rotation-to-healpix-map-in-healpy

    nside = hp.npix2nside(len(hpmap))

    # Get theta, phi for non-rotated map
    t,p = hp.pix2ang(nside, np.arange(hp.nside2npix(nside)))

    # Define a rotator
    if len(transf) == 2:
        r = hp.Rotator(coord=transf)
    else:
        r = hp.Rotator(deg=True, rot=[phideg,thetadeg])

    # Get theta, phi under rotated co-ordinates
    trot, prot = r(t,p)

    # Interpolate map onto these co-ordinates
    rot_map = hp.get_interp_val(hpmap, trot, prot)

    return rot_map

def build_priority_map(high_priority_regions, regions_outside_plane,
                        hp_log_star_density, npix, write_maps=False):
    """Function to build a survey footprint HEALpix map, estimating the
    approximate scientific priority of each pixel for galactic science, based on
    a combination of regions selected by stellar density plus selected regions
    of special scientific interest.  If a White Paper included a given HEALpix
    within its specified region of interest, this effectively consititutes
    a vote for that HEALpix.  Since the filter selection requested also varied
    between different science cases, votes for each pixel are tallied separately
    for each filter, creating different maps.
    Lastly, the different science cases place different degrees of priority on
    different filters.  For example Street et al. emphasizes observations in
    g,r,i,z over u and y.  This is represented as different filter_weights,
    specified for each science case.  """

    # Galactic Plane
    # Several white papers described overlapping regions in the Galactic Plane.
    # Almost all of this science depends on observations of the largest numbers
    # of stars possible, over as wide a range of galactic longitude as possible.
    # To represent these science cases, the priority for this region is estimated
    # based on the density of stars within each HEALpix.
    #
    # This dictionary defines as keys a set of thresholds in stellar density,
    # with corresponding values indicating the relative priority of pixels of
    # that density; this ensures lower priority to less-dense star fields.
    density_thresholds = { 0.60: 0.8, 0.70: 0.9, 0.80: 1.0 }

    # Each HEALpix is weighted according to the filter preferences specified:
    filterset_gp = high_priority_regions['Galactic_Plane']['filterset']

    # Build vote maps in each filter based on the stellar density of each HEALpix
    vote_maps = {}
    for f, filter_weight in filterset_gp.items():
        vote_maps[f] = np.zeros(npix)
        for threshold, location_weight in density_thresholds.items():
            idx = np.where(hp_log_star_density >= threshold*hp_log_star_density.max())[0]
            vote_maps[f][idx] += location_weight * filter_weight

    # Now we add the votes for HEALpix in regions of special scientific interest
    # for each filter
    for name, region in regions_outside_plane.items():
        for f, filter_weight in region['filterset'].items():
            vote_maps[f][region['pixel_region']] += filter_weight * 1.0

    if write_maps:
        # Output the priority maps in both PNG and FITS formats
        for f in filterset_gp.keys():
            current_max = vote_maps[f].max()*1.0
            #norm = vote_maps[f].max()
            #vote_maps[f] = vote_maps[f]/norm
            fig = plt.figure(3,(10,10))
            hp.mollview(vote_maps[f], title="Priority regions of the Galactic Plane, "+str(f)+"-band",
                        min=0.0, max=1.0)
            hp.graticule()
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_DIR,'priority_GalPlane_footprint_map_'+str(f)+'.png'))
            plt.close(3)

            hp.write_map(os.path.join(OUTPUT_DIR,'GalPlane_priority_map_'+str(f)+'.fits'),
                         vote_maps[f], overwrite=True)
    return vote_maps

if __name__ == '__main__':
    generate_maps()
