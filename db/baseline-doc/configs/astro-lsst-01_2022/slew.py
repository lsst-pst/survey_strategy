import lsst.sims.ocs.configuration.instrument.slew
assert type(config)==lsst.sims.ocs.configuration.instrument.slew.Slew, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.slew.Slew' % (type(config).__module__, type(config).__name__)
# Prerequisite list for telescope optics closed loop corrections.
config.prereq_telopticsclosedloop=['domalt', 'domazsettle', 'telsettle', 'readout', 'telopticsopenloop', 'filter', 'telrot']

# Prerequisite list for telescope azimuth movement.
config.prereq_telaz=[]

# Prerequisite list for filter movement.
config.prereq_filter=[]

# Prerequisite list for telescope settle time.
config.prereq_telsettle=['telalt', 'telaz']

# Prerequisite list for the dome settle time.
config.prereq_domazsettle=['domaz']

# Prerequisite list for the guider adq?
config.prereq_guider_adq=[]

# Prerequisite list for dome altitude movement.
config.prereq_domalt=[]

# Prerequisite list for telescope altitude movement.
config.prereq_telalt=[]

# Prerequisite list for telescope optics open loop corrections.
config.prereq_telopticsopenloop=['telalt', 'telaz']

# Prerequisite list for the ADC
config.prereq_adc=[]

# Prerequisite list for exposure time.
config.prereq_exposures=['telopticsclosedloop']

# Prerequisite list for the guider positioning.
config.prereq_guider_pos=[]

# Prerequisite list for dome azimuth movement.
config.prereq_domaz=[]

# Prerequisite list for camera electronics readout time.
config.prereq_readout=[]

# Prerequisite list for instrument optics.
config.prereq_ins_optics=[]

# Prerequisite list for telescope rotator movement.
config.prereq_telrot=[]

