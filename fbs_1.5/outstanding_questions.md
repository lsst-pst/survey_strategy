# Outstanding Questions for LSST Cadence simulations

With the release of [75 new survey simulations in v1.4](https://community.lsst.org/t/january-2020-update-fbs-1-4-runs/4006), we are now ready to start combining strategies to construct the first version of the LSST scheduler.

Here we list some outstanding questions where we would appriciate feedback from the community. When relevant, we list which simulations could be helpful answer these questions.

## Which deep drilling strategy should we employ?

We have several DDF strategies (baseline, DESC, AGN, Euclid). There are also proposals to ephasize a DDF in a single year, and de-emphasize other years.  What DDF observing strategy should be included in our simulations?

## What's the best dithering strategy for the DDFs (both spatially and rotationally)?

There is tension in that DM generally prefers larger dithers for calibration and co-addition purposes, while science cases prefer smaller dithers to preserve the area that reaches the deepest levels.


## What is the best camera rotational dithering strategy?

In the baseline, we set the camera rotator to a random position between -80 and 80 degrees (relative to the telescope) each night. We also test constraining the camera to be +/- 45 degrees to make diffraction spikes fall along CCD rows and columns.  

## What should the final survey footprint be?

We have run a large number of potential survey footprints.

Relevant sub-questions:  

* How the total number of visits should be distributed between filters.  
* Should we use dust extinction maps to define regions?
* Should we de-emphasize the galactic anti-center?
* Should we include some minimal coverage of the entire accesable sky for ToO potential?
* How much contingency should we have on the WFD region? The SRD states we should reach 825 visits, how far over this value should our simulations end up?

## Do we need to use a rolling cadence?

Rolling cadence makes it possible to better sample light curves of transient and variable objects in alternating years. 

## Should we use variable exposure times?

We can vary the exposure times based on the observing conditions to help keep individual exposures to similar depths.

## Should visits be 1x30s or 2x15s?

This probably has to wait until we have on-sky data. But it represent a fairly large loss of the total available time (7%) if we need to take two snaps per visit.

## Should we intentionally take observations at high airmass to measure DCR

For the bluer filters, DCR can make image template construction complicated. There is also potential to do science via measuring the DCR amplitude of certain objects (AGN, etc).

## What is the best strategy for taking observations in pairs?

We typically try to take pairs seperated by 22 minutes, and in different filters. It would be nice to know which colors are most useful.

## Should we use some of twilight time for a NEO survey?

## Should we include a short exposure time survey as well as the standard 30s visits?

We tested mixing in observations of 5s and 1s in addition to the usual survey.

## What's the best way to observe the LMC and SMC?

We have simulations where we include them as part of the WFD area, but we could also treat them as DDFs for more specific cadence

## Should we prioritize collecting "good seeing" images across the entire sky? In which filters?

We do not take much account of the atmospheric seeing. 
Other surveys have often preferentially observed certain filters in "good seeing" conditions.  

## Should we adjust the survey footprint slightly to account for over/under subscription?

Right now, we tend to use straight cuts in declination to define the survey area (easy to code and calculate areas covered). However, because of variable night length, weather downtime, and the placement of DDFs we have some regions of the sky that are oversubscribed and some (like the galactic plane) are undersubscribed. We could alter the limits of the WFD area to constrict in parts of the sky that are over-subscribed and flare where it is undersubscribed. This should result in a slightly more uniform WFD depth. 

## Do periodic sources suffer from aliasing?

The Bell et al white paper discussed scheduling to prevent aliasing of periodic sources. This is potentially a memory intensive problem to simulate. It would be good to see if there is a population of periodic sources that are currently suffering from aliasing and would drive a need to shift the timing of our observations?  Is there new science enabled by trying to avoid the current level of aliasing in LSST?

## Do we need to do anything more for image differencing templates?

Either for making sure we have enough templates early enough, or for DCR coverage.

## When/how should we optimize the basis function weights?

We can refine the behavior of the scheduler by varying the weights on the basis functions, namely the 5$\sigma$ depth, footprint, slewtime, filter, and template weights. Can we put together a combination of science metrics to judge the best combination in this 5D parameter space?

