import lsst.sims.ocs.configuration.instrument.obs_variation
assert type(config)==lsst.sims.ocs.configuration.instrument.obs_variation.ObservatoryVariation, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.obs_variation.ObservatoryVariation' % (type(config).__module__, type(config).__name__)
# Apply the observatory variational model.
config.apply_variation=False

# Change (units=percent) in the telescope kinematic parameters over the life of the survey.
config.telescope_change=0.0

# Change (units=percent) in the dome kinematic parameters over the life of the survey.
config.dome_change=0.0

