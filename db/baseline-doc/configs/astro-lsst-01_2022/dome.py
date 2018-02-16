import lsst.sims.ocs.configuration.instrument.dome
assert type(config)==lsst.sims.ocs.configuration.instrument.dome.Dome, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.dome.Dome' % (type(config).__module__, type(config).__name__)
# Maximum speed (units=degrees/second) of dome altitude movement.
config.altitude_maxspeed=1.75

# Maximum speed (units=degrees/second) of dome azimuth movement.
config.azimuth_maxspeed=1.5

# Maximum acceleration (units=degrees/second**2) of dome altitude movement.
config.altitude_accel=0.875

# Maximum deceleration (units=degrees/second**2) of dome azimuth movement.
config.azimuth_decel=0.75

# Maximum acceleration (units=degrees/second**2) of dome azimuth movement.
config.azimuth_accel=0.75

# Times (units=seconds) for the dome to settle after stopping.
config.settle_time=1.0

# Maximum deceleration (units=degrees/second**2) of dome altitude movement.
config.altitude_decel=0.875

