import lsst.sims.ocs.configuration.instrument.rotator
assert type(config)==lsst.sims.ocs.configuration.instrument.rotator.Rotator, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.rotator.Rotator' % (type(config).__module__, type(config).__name__)
# Maximum speed (units=degrees/second) of rotator movement.
config.maxspeed=3.5

# Minimum position (units=degrees) of rotator.
config.minpos=-90.0

# Position (units=degrees) of rotator to allow filter changes.
config.filter_change_pos=0.0

# Maximum acceleration (units=degrees/second**2) of rotator movement.
config.accel=1.0

# Maximum deceleration (units=degrees/second**2) of rotator movement.
config.decel=1.0

# Flag that if True enables the movement of the rotator during slews to put North-Up. If range is insufficient, then the alignment is North-Down. If the flag is False, then the rotator does not move during the slews, it is only tracking during the exposures.
config.follow_sky=False

# Flag that if True enables the rotator to keep the image angle after a filter change, moving back the rotator to the previous angle after the rotator was placed in filter change position. If the flag is False, then the rotator is left in the filter change position.
config.resume_angle=False

# Maximum position (units=degrees) of rotator.
config.maxpos=90.0

