## Constraints on the observing strategy ##

Important! This is a work in progress. We are gathering constraints here, but these should not yet be considered finalized or comprehensive.  There is also an important difference to consider between requirements (especially minimum specs) and expected performance, which could be better than those requirements. In cases where we do not have solid information on expected performance, we are quoting requirements.

For the official requirements on the Telescope & Site subsystems, please see [LSE-60](https://docushare.lsst.org/docushare/dsweb/Get/LSE-60) and for the requirements for the Camera subsystem, please see [LSE-59](https://docushare.lsst.org/docushare/dsweb/Get/LSE-59). 


### Pointing constraints ###

- Elevation limits: 20 to 86.5 degrees (with sidereal tracking).
These elevation limits are based on constraints on sidereal tracking capabilities. The telescope can point anywhere from 0 to 90 degrees in elevation, but will only track at elevations between 20 to 86.5 degrees.

- Slew times.
There are constraints on the slew capabilities; these are encapsulated in the lsst-ts:ts_observatory_model software package. Roughly speaking, a close-by field requires 5s to slew to, a very distant field could take several minutes. Slews where the elevation changes by more than 9 degrees require a closed optics loop correction which takes an additional 36s (note: current simulations use a 20s delay for the closed optics loop correction and this is still the current requirement; there is a change-control request in progress to update this to 36s).

- Moon avoidance angle: 30 degrees.
The current moon-avoidance angle is 30 degrees, based on scattered light simulations from systems engineering.
This is not a physical constraint as much as a 'best practices to avoid scattered light' constraint.

### Filter change constraints ###

- Filter change time: 120s.
This includes 90s for the filter change mechanism and up to 30s to rotate the camera to align the filter changer with gravity.

- Number of filter changes.
The total number of filter changes must be less than 100,000 over 15 years. This translates to about 18 per night.

- Available filters: 5.
5 filters can be held in the filter changer at one time. The 6th filter must swap in and out. These filter swaps are expected to be done in daytime, and are limited to 3000 over 15 years, or about once every two days. The filter swap procedure requires at least 1.5 hours.


### Exposure constraints ###

- Minimum exposure time: 1s. It is not clear if the PSF is well-formed enough for difference imaging at this exposure time.

- Maximum exposure time: Undetermined, however at 150s, stars will saturate at about 18.3. At this magnitude, it is unclear how many stars may overlap with existing catalogs for calibration or template purposes, nor is it clear the effect on CR rejection.

- Sequences of short exposures.
Sequences of short exposures (<15s) without breaks (such as a 5s slew) can cause thermal problems for the camera. No more than X exposures of <15s should be taken without a slew or other pause. [??]


### Data processing constraints ###

- Data Management pipelines may be reconfigured for minisurvey processing, but special processing beyond this is the responsibility of the science community. (??)


### Survey constraints ###

- The footprint for the WFD must be at least X with X visits per field. The cadence for these observations is still flexible, and the footprint for the WFD may vary from X to X.

- SRD requirements on WFD (implications about time baseline for WFD?)

- Deep drilling field positions.
4 of the potential deep drilling fields have been announced; these positions are fixed. The number of remaining deep drilling fields and their cadence of observations is still flexible.

- Minisurvey observations.
The current baseline includes Deep Drilling, North Ecliptic Spur, Galactic Plane, and South Celestial Pole regions as minisurveys. There are many good reasons to include these regions, however their observation (or even, lack of observation) is flexible and part of the driver for this call for white papers.
