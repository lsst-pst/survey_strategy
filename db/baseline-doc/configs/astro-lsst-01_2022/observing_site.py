import lsst.sims.ocs.configuration.obs_site
assert type(config)==lsst.sims.ocs.configuration.obs_site.ObservingSite, 'config is of type %s.%s instead of lsst.sims.ocs.configuration.obs_site.ObservingSite' % (type(config).__module__, type(config).__name__)
# Telescope site name.
config.name='Cerro Pachon'

# Telescope site's atmospheric pressure (units=millibars)
config.pressure=750.0

# Telescope site's Longitude (units=degrees), negative implies West
config.longitude=-70.7494

# Telescope site's Elevation (units=meters above sea level)
config.height=2650.0

# Telescope site's relative humidity (units=percent)
config.relative_humidity=0.4

# Telescope site's Latitude (units=degrees), negative implies South.
config.latitude=-30.2444

# Telescope site's atmospheric temperature (units=degrees C)
config.temperature=11.5

