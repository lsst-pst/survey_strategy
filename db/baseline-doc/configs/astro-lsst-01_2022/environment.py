import lsst.sims.ocs.configuration.environment
assert type(config)==lsst.sims.ocs.configuration.environment.Environment, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.environment.Environment' % (type(config).__module__, type(config).__name__)
# Alternate database file for the seeing. Must have same format as internal database.
config.cloud_db=''

# Scale factor to convert geometric seeing to effective seeing.
config.geom_eff_factor=1.04

# Alternate database file for the seeing. Must have same format as internal database.
config.seeing_db=''

# Design value of the camera contribution to the seeing (units=arcseconds).
config.camera_seeing=0.3

# Design value of the telescope contribution to the seeing (units=arcseconds).
config.telescope_seeing=0.25

# Design value of the optical path contribution to the seeing (units=arcseconds).
config.optical_design_seeing=0.08

# Scale factor to convert seeing to effective.
config.scale_to_eff=1.16

