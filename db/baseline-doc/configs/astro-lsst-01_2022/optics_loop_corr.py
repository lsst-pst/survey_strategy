import lsst.sims.ocs.configuration.instrument.optics_loop_corr
assert type(config)==lsst.sims.ocs.configuration.instrument.optics_loop_corr.OpticsLoopCorr, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.optics_loop_corr.OpticsLoopCorr' % (type(config).__module__, type(config).__name__)
# Altitude (units=degrees) limits for the delay ranges.
config.tel_optics_cl_alt_limit=[0.0, 9.0, 90.0]

# Delay factor for Open Loop optics correction (units=seconds/degrees in ALT slew)
config.tel_optics_ol_slope=0.2857142857142857

# Time delay (units=seconds) for the corresponding ALT slew range in the Closed Loop optics correction.
config.tel_optics_cl_delay=[0.0, 20.0]

