import lsst.sims.ocs.configuration.instrument.telescope
assert type(config)==lsst.sims.ocs.configuration.instrument.telescope.Telescope, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.telescope.Telescope' % (type(config).__module__, type(config).__name__)
# Maximum speed (units=degrees/second) of telescope altitude movement.
config.altitude_maxspeed=3.5

# The minimum altitude of the telescope from horizon (units=degrees)
config.altitude_minpos=20.0

# Maximum acceleration (units=degrees/second**2) of telescope altitude movement.
config.altitude_accel=3.5

# Maximum deceleration (units=degrees/second**2) of telescope azimuth movement.
config.azimuth_decel=7.0

# Maximum acceleration (units=degrees/second**2) of telescope azimuth movement.
config.azimuth_accel=7.0

# The maximum altitude of the telescope for zenith avoidance (units=degrees)
config.altitude_maxpos=86.5

# Time (units=seconds) for the telescope mount to settle after stopping.
config.settle_time=3.0

# Maximum absolute azimuth limit (units=degrees) of telescope.
config.azimuth_maxpos=270.0

# Maximum speed (units=degrees/second) of telescope azimuth movement.
config.azimuth_maxspeed=7.0

# Minimum absolute azimuth limit (units=degrees) of telescope.
config.azimuth_minpos=-270.0

# Maximum deceleration (units=degrees/second**2) of telescope altitude movement.
config.altitude_decel=3.5

