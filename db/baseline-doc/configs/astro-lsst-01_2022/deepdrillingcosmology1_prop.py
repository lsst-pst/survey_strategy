import lsst.sims.ocs.configuration.science.deep_drilling_cosmology1
assert type(config)==lsst.sims.ocs.configuration.science.deep_drilling_cosmology1.DeepDrillingCosmology1, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.science.deep_drilling_cosmology1.DeepDrillingCosmology1' % (type(config).__module__, type(config).__name__)
# The maximum airmass allowed for any field.
config.sky_constraints.max_airmass=1.5

# The maximum fraction of clouds allowed for any field.
config.sky_constraints.max_cloud=0.7

# Flag to use 2 degree exclusion zone around bright planets.
config.sky_constraints.exclude_planets=True

# The minimum distance (units=degrees) from the moon a field must be.
config.sky_constraints.min_distance_moon=30.0

# Name for the proposal.
config.name='DeepDrillingCosmology1'

# Sky user regions for the proposal as a list of field Ids.
config.sky_user_regions=[290, 744, 1427, 2412, 2786]

config.sub_sequences={}
config.sub_sequences[0]=lsst.sims.ocs.configuration.proposal.sub_sequence.SubSequence()
# Time (units=seconds) between subsequent visits for a field/filter combination. Must be non-zero if number of grouped visits is greater than one.
config.sub_sequences[0].time_interval=259200.0

# The number of visits required for each filter in the sub-sequence.
config.sub_sequences[0].visits_per_filter=[20, 10, 20, 26, 20]

# Relative time when the window reaches maximum rank for subsequent grouped visits.
config.sub_sequences[0].time_window_max=1.0

# The number of required events for the sub-sequence.
config.sub_sequences[0].num_events=27

# The maximum number of events the sub-sequence is allowed to miss.
config.sub_sequences[0].num_max_missed=0

# Weighting factor for scaling the shape of the time window.
config.sub_sequences[0].time_weight=1.0

# The list of filters required for the sub-sequence.
config.sub_sequences[0].filters=['r', 'g', 'i', 'z', 'y']

# Relative time when the window opens for subsequent grouped visits.
config.sub_sequences[0].time_window_start=0.8

# Relative time when the window ends for subsequent grouped visits.
config.sub_sequences[0].time_window_end=1.4

# The identifier for the sub-sequence.
config.sub_sequences[0].name='main'

config.sub_sequences[1]=lsst.sims.ocs.configuration.proposal.sub_sequence.SubSequence()
# Time (units=seconds) between subsequent visits for a field/filter combination. Must be non-zero if number of grouped visits is greater than one.
config.sub_sequences[1].time_interval=86400.0

# The number of visits required for each filter in the sub-sequence.
config.sub_sequences[1].visits_per_filter=[20]

# Relative time when the window reaches maximum rank for subsequent grouped visits.
config.sub_sequences[1].time_window_max=1.0

# The number of required events for the sub-sequence.
config.sub_sequences[1].num_events=7

# The maximum number of events the sub-sequence is allowed to miss.
config.sub_sequences[1].num_max_missed=0

# Weighting factor for scaling the shape of the time window.
config.sub_sequences[1].time_weight=1.0

# The list of filters required for the sub-sequence.
config.sub_sequences[1].filters=['u']

# Relative time when the window opens for subsequent grouped visits.
config.sub_sequences[1].time_window_start=0.8

# Relative time when the window ends for subsequent grouped visits.
config.sub_sequences[1].time_window_end=1.4

# The identifier for the sub-sequence.
config.sub_sequences[1].name='u-band'

config.filters={}
config.filters['g']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['g'].bright_limit=19.5

# Darkest magnitude limit for filter.
config.filters['g'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['g'].max_seeing=1.5

# Band name of the filter.
config.filters['g'].name='g'

# The list of exposure times (units=seconds) for the filter
config.filters['g'].exposures=[15.0, 15.0]

config.filters['i']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['i'].bright_limit=19.5

# Darkest magnitude limit for filter.
config.filters['i'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['i'].max_seeing=1.5

# Band name of the filter.
config.filters['i'].name='i'

# The list of exposure times (units=seconds) for the filter
config.filters['i'].exposures=[15.0, 15.0]

config.filters['r']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['r'].bright_limit=19.5

# Darkest magnitude limit for filter.
config.filters['r'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['r'].max_seeing=1.5

# Band name of the filter.
config.filters['r'].name='r'

# The list of exposure times (units=seconds) for the filter
config.filters['r'].exposures=[15.0, 15.0]

config.filters['u']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['u'].bright_limit=21.3

# Darkest magnitude limit for filter.
config.filters['u'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['u'].max_seeing=1.5

# Band name of the filter.
config.filters['u'].name='u'

# The list of exposure times (units=seconds) for the filter
config.filters['u'].exposures=[15.0, 15.0]

config.filters['y']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['y'].bright_limit=17.5

# Darkest magnitude limit for filter.
config.filters['y'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['y'].max_seeing=1.5

# Band name of the filter.
config.filters['y'].name='y'

# The list of exposure times (units=seconds) for the filter
config.filters['y'].exposures=[15.0, 15.0]

config.filters['z']=lsst.sims.ocs.configuration.proposal.band_filter.BandFilter()
# Brightest magnitude limit for filter.
config.filters['z'].bright_limit=17.5

# Darkest magnitude limit for filter.
config.filters['z'].dark_limit=30.0

# The maximum seeing limit for filter
config.filters['z'].max_seeing=1.5

# Band name of the filter.
config.filters['z'].name='z'

# The list of exposure times (units=seconds) for the filter
config.filters['z'].exposures=[15.0, 15.0]

# Flag to restart sequences that were lost due to observational constraints.
config.scheduling.restart_lost_sequences=True

# Bonus to apply to fields giving precedence to low arimass ones. Bonus runs from 0 to 1.
config.scheduling.airmass_bonus=0.0

# Bonus to apply to fields giving precedence to fields near the meridian. Bonus runs from 0 to 1.
config.scheduling.hour_angle_bonus=0.3

# The maximum number of visits requested for the proposal over the lifetime of the survey. This effects the time-balancing for the proposal, but does not prevent more visits from being taken.
config.scheduling.max_visits_goal=250000

# Flag to determine if consecutive visits are accepted.
config.scheduling.accept_consecutive_visits=True

# Flag to restart sequences that were already completed.
config.scheduling.restart_complete_sequences=True

# Maximum hour angle (units=hours) for the bonus factor calculation. Hour angles larger will cause the bonus to be negative. Range is 0.1 to 12.
config.scheduling.hour_angle_max=6.0

# The maximum number of targets the proposal will propose.
config.scheduling.max_num_targets=100

# Flag to determine if observations other than proposal's top target are accepted.
config.scheduling.accept_serendipity=False

# The sun altitude (units=degrees) for twilight consideration.
config.sky_nightly_bounds.twilight_boundary=-12.0

# LST extent (units=degrees) before sunset LST (-) and after sunrise LST (+) for providing a region of the sky to select.
config.sky_nightly_bounds.delta_lst=60.0

config.master_sub_sequences={}
# Angle (units=degrees) around the observing site's latitude for which to create a Declination window for field selection.
config.sky_exclusion.dec_window=90.0

config.sky_exclusion.selections={}
