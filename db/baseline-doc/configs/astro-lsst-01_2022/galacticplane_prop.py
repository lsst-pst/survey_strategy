import lsst.sims.ocs.configuration.science.galactic_plane
assert type(config)==lsst.sims.ocs.configuration.science.galactic_plane.GalacticPlane, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.galactic_plane.GalacticPlane' % (type(config).__module__, type(config).__name__)
# The maximum airmass allowed for any field.
config.sky_constraints.max_airmass=2.5

# The maximum fraction of clouds allowed for any field.
config.sky_constraints.max_cloud=0.7

# Flag to use 2 degree exclusion zone around bright planets.
config.sky_constraints.exclude_planets=True

# The minimum distance (units=degrees) from the moon a field must be.
config.sky_constraints.min_distance_moon=30.0

# Name for the proposal.
config.name='GalacticPlane'

# A list of logical operations [and, or] that combine the region selections. Must be one less than the number of selections. If only one region, the list is left empty.
config.sky_region.combiners=[]

config.sky_region.selection_mapping=None
config.sky_region.selections={}
config.sky_region.selections[0]=lsst.sims.ocs.configuration.proposal.selection.Selection()
# Maximum limit (units=degrees) for field selection.
config.sky_region.selections[0].maximum_limit=10.0

# Minimum limit (units=degrees) for field selection.
config.sky_region.selections[0].minimum_limit=0.0

# Type of coordinate to select.
config.sky_region.selections[0].limit_type='GP'

# Boundary limit (units=degrees) for a sloping envelope selection.
config.sky_region.selections[0].bounds_limit=90.0

config.sky_region.time_ranges=None
config.filters={}
config.filters['g']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['g'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['g'].bright_limit=20.8

# Band name of the filter.
config.filters['g'].name='g'

# The number of grouped (in a night) visits for the filter.
config.filters['g'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['g'].num_visits=30

# The maximum seeing limit for filter
config.filters['g'].max_seeing=3.0

# The list of exposure times (units=seconds) for the filter
config.filters['g'].exposures=[15.0, 15.0]

config.filters['i']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['i'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['i'].bright_limit=19.5

# Band name of the filter.
config.filters['i'].name='i'

# The number of grouped (in a night) visits for the filter.
config.filters['i'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['i'].num_visits=30

# The maximum seeing limit for filter
config.filters['i'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['i'].exposures=[15.0, 15.0]

config.filters['r']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['r'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['r'].bright_limit=20.0

# Band name of the filter.
config.filters['r'].name='r'

# The number of grouped (in a night) visits for the filter.
config.filters['r'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['r'].num_visits=30

# The maximum seeing limit for filter
config.filters['r'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['r'].exposures=[15.0, 15.0]

config.filters['u']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['u'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['u'].bright_limit=20.8

# Band name of the filter.
config.filters['u'].name='u'

# The number of grouped (in a night) visits for the filter.
config.filters['u'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['u'].num_visits=30

# The maximum seeing limit for filter
config.filters['u'].max_seeing=3.0

# The list of exposure times (units=seconds) for the filter
config.filters['u'].exposures=[15.0, 15.0]

config.filters['y']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['y'].dark_limit=21.4

# Brightest magnitude limit for filter.
config.filters['y'].bright_limit=16.0

# Band name of the filter.
config.filters['y'].name='y'

# The number of grouped (in a night) visits for the filter.
config.filters['y'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['y'].num_visits=30

# The maximum seeing limit for filter
config.filters['y'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['y'].exposures=[15.0, 15.0]

config.filters['z']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['z'].dark_limit=21.4

# Brightest magnitude limit for filter.
config.filters['z'].bright_limit=17.0

# Band name of the filter.
config.filters['z'].name='z'

# The number of grouped (in a night) visits for the filter.
config.filters['z'].num_grouped_visits=1

# The number of requested visits for the filter.
config.filters['z'].num_visits=30

# The maximum seeing limit for filter
config.filters['z'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['z'].exposures=[15.0, 15.0]

# Time (units=seconds) between subsequent visits for a field/filter combination. Must be non-zero if number of grouped visits is greater than one.
config.scheduling.time_interval=0.0

# Maximum hour angle (units=hours) for the bonus factor calculation. Hour angles larger will cause the bonus to be negative. Range is 0.1 to 12.
config.scheduling.hour_angle_max=3.0

# Bonus to apply to fields giving precedence to low arimass ones. Bonus runs from 0 to 1.
config.scheduling.airmass_bonus=0.0

# Bonus to apply to fields giving precedence to fields near the meridian. Bonus runs from 0 to 1.
config.scheduling.hour_angle_bonus=0.3

# Flag to determine if consecutive visits are accepted.
config.scheduling.accept_consecutive_visits=False

# Flag to restrict the number of grouped visits per night to the requested number.
config.scheduling.restrict_grouped_visits=True

# Weighting factor for scaling the shape of the time window.
config.scheduling.time_weight=0.0

# Relative time when the window reaches maximum rank for subsequent grouped visits.
config.scheduling.time_window_max=0.0

# The maximum number of targets the proposal will propose.
config.scheduling.max_num_targets=100

# Relative time when the window opens for subsequent grouped visits.
config.scheduling.time_window_start=0.0

# Flag to determine if observations other than proposal's top target are accepted.
config.scheduling.accept_serendipity=False

# Relative time when the window ends for subsequent grouped visits.
config.scheduling.time_window_end=0.0

# The sun altitude (units=degrees) for twilight consideration.
config.sky_nightly_bounds.twilight_boundary=-12.0

# LST extent (units=degrees) before sunset LST (-) and after sunrise LST (+) for providing a region of the sky to select.
config.sky_nightly_bounds.delta_lst=60.0

# Angle (units=degrees) around the observing site's latitude for which to create a Declination window for field selection.
config.sky_exclusion.dec_window=90.0

config.sky_exclusion.selections={}
