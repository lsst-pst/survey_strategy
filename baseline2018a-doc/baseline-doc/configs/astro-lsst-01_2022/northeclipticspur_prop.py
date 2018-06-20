import lsst.sims.ocs.configuration.science.north_ecliptic_spur
assert type(config)==lsst.sims.ocs.configuration.science.north_ecliptic_spur.NorthEclipticSpur, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.north_ecliptic_spur.NorthEclipticSpur' % (type(config).__module__, type(config).__name__)
# The maximum airmass allowed for any field.
config.sky_constraints.max_airmass=2.5

# The maximum fraction of clouds allowed for any field.
config.sky_constraints.max_cloud=0.7

# Flag to use 2 degree exclusion zone around bright planets.
config.sky_constraints.exclude_planets=True

# The minimum distance (units=degrees) from the moon a field must be.
config.sky_constraints.min_distance_moon=30.0

# Name for the proposal.
config.name='NorthEclipticSpur'

# A list of logical operations [and, or] that combine the region selections. Must be one less than the number of selections. If only one region, the list is left empty.
config.sky_region.combiners=['and']

config.sky_region.selection_mapping=None
config.sky_region.selections={}
config.sky_region.selections[0]=lsst.sims.ocs.configuration.proposal.selection.Selection()
# Maximum limit (units=degrees) for field selection.
config.sky_region.selections[0].maximum_limit=10.0

# Minimum limit (units=degrees) for field selection.
config.sky_region.selections[0].minimum_limit=-30.0

# Type of coordinate to select.
config.sky_region.selections[0].limit_type='EB'

# Boundary limit (units=degrees) for a sloping envelope selection.
config.sky_region.selections[0].bounds_limit=float('nan')

config.sky_region.selections[1]=lsst.sims.ocs.configuration.proposal.selection.Selection()
# Maximum limit (units=degrees) for field selection.
config.sky_region.selections[1].maximum_limit=90.0

# Minimum limit (units=degrees) for field selection.
config.sky_region.selections[1].minimum_limit=2.8

# Type of coordinate to select.
config.sky_region.selections[1].limit_type='Dec'

# Boundary limit (units=degrees) for a sloping envelope selection.
config.sky_region.selections[1].bounds_limit=float('nan')

config.sky_region.time_ranges=None
config.filters={}
config.filters['i']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['i'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['i'].bright_limit=19.5

# Band name of the filter.
config.filters['i'].name='i'

# The number of grouped (in a night) visits for the filter.
config.filters['i'].num_grouped_visits=2

# The number of requested visits for the filter.
config.filters['i'].num_visits=92

# The maximum seeing limit for filter
config.filters['i'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['i'].exposures=[15.0, 15.0]

config.filters['r']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['r'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['r'].bright_limit=20.25

# Band name of the filter.
config.filters['r'].name='r'

# The number of grouped (in a night) visits for the filter.
config.filters['r'].num_grouped_visits=2

# The number of requested visits for the filter.
config.filters['r'].num_visits=92

# The maximum seeing limit for filter
config.filters['r'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['r'].exposures=[15.0, 15.0]

config.filters['z']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['z'].dark_limit=21.0

# Brightest magnitude limit for filter.
config.filters['z'].bright_limit=17.0

# Band name of the filter.
config.filters['z'].name='z'

# The number of grouped (in a night) visits for the filter.
config.filters['z'].num_grouped_visits=2

# The number of requested visits for the filter.
config.filters['z'].num_visits=80

# The maximum seeing limit for filter
config.filters['z'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['z'].exposures=[15.0, 15.0]

config.filters['g']=lsst.sims.ocs.configuration.proposal.general_band_filter.GeneralBandFilter()
# Darkest magnitude limit for filter.
config.filters['g'].dark_limit=30.0

# Brightest magnitude limit for filter.
config.filters['g'].bright_limit=21.0

# Band name of the filter.
config.filters['g'].name='g'

# The number of grouped (in a night) visits for the filter.
config.filters['g'].num_grouped_visits=2

# The number of requested visits for the filter.
config.filters['g'].num_visits=40

# The maximum seeing limit for filter
config.filters['g'].max_seeing=2.0

# The list of exposure times (units=seconds) for the filter
config.filters['g'].exposures=[15.0, 15.0]

# Time (units=seconds) between subsequent visits for a field/filter combination. Must be non-zero if number of grouped visits is greater than one.
config.scheduling.time_interval=1800.0

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
config.scheduling.time_weight=1.0

# Relative time when the window reaches maximum rank for subsequent grouped visits.
config.scheduling.time_window_max=1.0

# The maximum number of targets the proposal will propose.
config.scheduling.max_num_targets=100

# Relative time when the window opens for subsequent grouped visits.
config.scheduling.time_window_start=0.5

# Flag to determine if observations other than proposal's top target are accepted.
config.scheduling.accept_serendipity=False

# Relative time when the window ends for subsequent grouped visits.
config.scheduling.time_window_end=2.0

# The sun altitude (units=degrees) for twilight consideration.
config.sky_nightly_bounds.twilight_boundary=-12.0

# LST extent (units=degrees) before sunset LST (-) and after sunrise LST (+) for providing a region of the sky to select.
config.sky_nightly_bounds.delta_lst=60.0

# Angle (units=degrees) around the observing site's latitude for which to create a Declination window for field selection.
config.sky_exclusion.dec_window=90.0

config.sky_exclusion.selections={}
