import lsst.sims.ocs.configuration.downtime
assert type(config)==lsst.sims.ocs.configuration.downtime.Downtime, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.downtime.Downtime' % (type(config).__module__, type(config).__name__)
# A placeholder for the random seed used when one is requested. This is only available in the saved config.
config.unscheduled_downtime_random_seed=1516231120

# Use a random seed determining the unscheduled downtime rather than fixed seed.
config.unscheduled_downtime_use_random_seed=False

# Alternate database file for scheduled downtime. Must have same format as internal database.
config.scheduled_downtime_db=''

