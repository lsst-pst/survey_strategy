import lsst.sims.ocs.configuration.scheduler_driver
assert type(config)==lsst.sims.ocs.configuration.scheduler_driver.SchedulerDriver, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.scheduler_driver.SchedulerDriver' % (type(config).__module__, type(config).__name__)
# The weighting value to apply to the slew time cost function result.
config.timecost_weight=1.0

# Solar altitude (degrees) when it is considered night.
config.night_boundary=-12.0

# The weighting value to apply to the time balancing equations. This parameter should be greater than or equal to zero.
config.propboost_weight=1.0

# Flag to detemine if cross-proposal time-balancing is used.
config.time_balancing=True

# New moon phase threshold for swapping to dark time filter.
config.new_moon_phase_threshold=20.0

# Flag to ignore sky brightness limits when rejecting targets.
config.ignore_sky_brightness=False

# Flag to ignore cloud limits when rejecting targets.
config.ignore_clouds=False

# The weighting value to apply to the filter change cost function result.
config.filtercost_weight=1.0

# Flag to ignore seeing limits when rejecting targets.
config.ignore_seeing=False

# Flag to ignore airmass limits when rejecting targets.
config.ignore_airmass=False

# Flag to determine if two identical field/filter targets have their ranks added and then considered as one target.
config.coadd_values=True

# The cost value associated with the time cost reference slew time.
config.timecost_cost_ref=0.3

# The slew time (units=seconds) where the time cost value equals one.
config.timecost_time_max=150.0

# The reference slew time (units=seconds) that sets the steepness of the cost function.
config.timecost_time_ref=5.0

