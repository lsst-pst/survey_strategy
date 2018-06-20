import lsst.sims.ocs.configuration.survey
assert type(config)==lsst.sims.ocs.configuration.survey.Survey, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.survey.Survey' % (type(config).__module__, type(config).__name__)
# The delay (units=seconds) to skip the simulation time forward when not receiving a target.
config.idle_delay=60.0

# The start date (format=YYYY-MM-DD) of the survey.
config.start_date='2022-10-01'

# The list of available sequence proposals.
config.sequence_proposals=['DeepDrillingCosmology1']

# The fractional duration (units=years) of the survey.
config.duration=10.0

# An alternative directory location for proposals.
config.alt_proposal_dir=None

# The list of available general proposals.
config.general_proposals=['GalacticPlane', 'NorthEclipticSpur', 'SouthCelestialPole', 'WideFastDeep']

