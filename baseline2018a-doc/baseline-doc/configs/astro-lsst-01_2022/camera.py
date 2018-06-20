import lsst.sims.ocs.configuration.instrument.camera
assert type(config)==lsst.sims.ocs.configuration.instrument.camera.Camera, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.camera.Camera' % (type(config).__module__, type(config).__name__)
# Time (units=seconds) for the camera shutter to open or close
config.shutter_time=1.0

# Minimum time (units=seconds) between filter changes in a night.
config.filter_max_changes_burst_time=0.0

# Maximum number of filter changes in a night.
config.filter_max_changes_burst_num=1

# Time (units=seconds) to mount a filter.
config.filter_mount_time=28800.0

# The list of filters that can be removed.
config.filter_removable=['y', 'z']

# Maximum time (units=seconds) for the average number of filter changes.
config.filter_max_changes_avg_time=31557600.0

# Time (units=seconds) for the camera electronics readout.
config.readout_time=2.0

# The list of unmounted but available to swap filters.
config.filter_unmounted=['u']

# Initial state for the mounted filters. Empty positions must be filled with id="" no (filter).
config.filter_mounted=['g', 'r', 'i', 'z', 'y']

# The currently mounted filter.
config.filter_pos='r'

# Maximum average number of filter changes per year.
config.filter_max_changes_avg_num=3000

# Time (units=seconds) to change a filter.
config.filter_change_time=120.0

