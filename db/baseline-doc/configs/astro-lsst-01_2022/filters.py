import lsst.sims.ocs.configuration.instrument.filters
assert type(config)==lsst.sims.ocs.configuration.instrument.filters.Filters, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.instrument.filters.Filters' % (type(config).__module__, type(config).__name__)
# The effective wavelength (units=nm) for the y filter calculated from the throughputs.
config.y_effective_wavelength=971.0

# The effective wavelength (units=nm) for the z filter calculated from the throughputs.
config.z_effective_wavelength=869.1

# The effective wavelength (units=nm) for the u filter calculated from the throughputs.
config.u_effective_wavelength=367.0

# The effective wavelength (units=nm) for the r filter calculated from the throughputs.
config.r_effective_wavelength=622.2

# The effective wavelength (units=nm) for the g filter calculated from the throughputs.
config.g_effective_wavelength=482.5

# The effective wavelength (units=nm) for the i filter calculated from the throughputs.
config.i_effective_wavelength=754.5

