# Notes on the v2.0 and v2.1 runs


Lots of radar plots etc in notebooks: https://github.com/lsst-sims/sims_featureScheduler_runs2.1/blob/main/maf/combined_look.ipynb and https://github.com/lsst-sims/sims_featureScheduler_runs2.0/blob/main/maf/combined_look.ipynb

## Baseline-like Runs ##

* New baseline includes rolling, which gives a substantial boost to SNe

* New baseline has increased bulge coverage, boosting microlensing

* The new footprint results in 4% decrease in fO metric


## Bluer ##


I think this was supposed to give a boost to SNe, but it looks pretty small. Seems to hurt Transients and WL.

## Long u-band exposures ##

Taking longer u-band exposures.  

* Both give a small boost to fO

* long_u1 hurts lots of science metrics, especially SNe and fast microlensing

* long_u2 is mostly neutral, but no obvious gains anywhere

## Rolling experiments ##

We test rolling with different fractions of the sky (half, third, sixth), and two different strengths (50% and 90%). 
Our baseline of half sky at 80-90% seems fairly close to ideal. Rolling with smaller area can boost SNe and TDE metrics, but at significant penalty for proper motions and faint NEOs.

Turning off rolling gives a modest boost to astrometry metrics, but is very bad for almost all transients. 

The `roll_early` tests the impact of adding an additional rolling season. This gives a nice boost to SNe and transients, with a small impact on proper motions. I guess I can point out that if the survey extends slightly, that proper motion precision can be recovered, but once the transients are gone, they are gone forever.

Adding rolling in the bulge doesn't have any perks. We might need more bulge-specific transient metrics.


## Long Gaps ##

The long gaps runs are a pretty clear trade off between the Transients metric and just about everything else. Also an odd effect that the Transients metric seems to get worse when the long gaps are off for 3 or more nights. The increase in the Transients metric seems fairly modest, it's tough to judge since it it a unitless score that increases from 180 to 190-195.

Taking long gaps with no initial pairs seems like a major loss across the board. 

## Presto ##

Presto with a 1.2 or 2.0 hour gap is terrible for everything (as expected). 

The 2.5, 3.0, 3.5, and 4.0 hour gaps show huge improvements for the Transient metric, but really hurt everything else, especially SNe and faint NEOs. 

No major difference between the mix and regular presto variants. Regular presto is (g+r, r+i, i+z), mix is (g+i, r+z, i+y). The mix version gets a little higher transient score at 4 hours, but does a little worse at 2.5 hours. 


The presto_half runs execute the presto triple strategy half of the nights. 


## Varied galactic plane ##

Pretty much just as expected. Giving less time to galactic plane helps cosmology metrics. Could use some more metrics that are sensitive to the galactic plane (we have microlensing, but not much else).


## Varied NES ##

Many of the solar system metrics are fairly insensitive to the fraction of time spent on the NES. I'll leave it to the solar system collaboration to make the case for where they think the optimal fraction is. Might be some potential to shave a little bit of time off of NES.

## Variable exposure time ##

Surprisingly hurts SNe, Transients, and faint NEOs. 

## North Stripe ##

Adding coverage to the north. Very minor impact on most metrics, but it would probably only help us recover a handful of ToO events. And we probably want to keep the ToO chasing in the WFD area as much as possible anyway.

## Carina ##

Very minor impact, as expected.

## Local Galaxies ##

Extra g,r,i observations on some local galaxies. Very minor impact on metrics. Would be nice to have a metric that confirms these do a better job on the nearby galaxies.

## short exposures ##

Including short exposures. Looks like we have short exposures and multiple short exposures. 
Multi short has a pretty large hit on SNe metric. We don't have metrics that show the value of short exposures. The multi-short is probably no longer feasible because shutter will heat up.

## Roman ##

Observing RGES field for microlensing. Indeed, makes the fast microlensing metric go up. Virtually zero impact on the rest of the survey. Looks like these were 0.07% of the total time. 

## Virgo ##

Include the virgo cluster in WFD footprint. Very minor. So minor we added this to the 2.1 baseline.

## SMC movie ##

Very minor impact. This came out to 0.13% of the visits.

## ToO ##

Looks like we tested chasing 10 or 50 ToOs per year. Minor impact on the science metrics.


# 2.1 Runs #

## DDF ##

The new DDF experiments 

We still need more DDF metrics. The QSO one we are running now is depth-only, doesn't seem to have any cadence sensitivity.

* For all the DDF-centric experiments, the final depths and number of visits are all comparable, typically plus/minus 0.1 mags. Can be outliers if the dither size is very large.

* Early pass with the AGN structure function uncertainty doesn't show much difference between runs. May need to tune kwarg parameters (e.g., what magnitude AGN should we be considering?)?

* Doing shorter DDF sequences more often can boost the SNe metrics considerably, but it does result in a lower open shutter fraction because it adds more filter changes. Might be worth looking at observing daily, but only in 2-3 filters rather than all 5. That could maybe maintain the SNe improvement but recover much of the open shutter fraction. 


Descriptions of each:

* ddf_season_length_:  Varying the season length of the DDFs
* ddf_double_: Half-length sequences twice as often, again varying season length
* ddf_accourd: Accordion cadence varying total season length, low-cadence season length, and the low cadence
* ddf_bright: Reduce constraint on when DDF sequences can be scheduled (allow shallow depth sequences to maintain cadence)
* ddf_deep_rolling: From DESC. Daily cadence, each field observed for 2 full seasons
* ddf_deep_u: The deep universal strategy from DESC. 
* ddf_dither: Vary the DDF dither size
* ddf_early_deep: From DESC, early deep rolling strategy with only 3 DDFs
* ddf_euclid_moved: Moving the Euclid field to test RA-oversubscription
* ddf_old_rot: Using the old camera rotational strategy
* ddf_quad: Quarter-length sequences executed 4x as often
* ddf_quad_subfilter: Like ddf_quad, but not doing all filters for each sequence to reduce filter change overhead
* ddf_roll: Initial attempt at rolling DDFs


## shave ##

Varying the exposure time of standard visits between 20 and 40 seconds. Going just slightly shorter in exposure time seems to have a large negative impact on the SNe metric, not sure why.

## Pencil Surveys ##

The `pencil_fs2` run boosts the transient metric, but has a fairly significant impact on fO and SNe. The open shutter fraction is down to 68%. This is from not enforcing contiguous blobs. 

The `pencil_fs1` run suffers from the scheduler not being able to easily connect some of the desired pencil beam areas with other parts of the survey. Currently no metrics show a significant improvement over the baseline. The open shutter fraction drops all the way down to 67%. 

If there's a compelling metric that shows improvement with these runs, we can work on extending the scheduler to selectively enforce contiguous blobs and recover most of the lost open shutter fraction. 

## Plane Priority ##

Run with pencil beam surveys on (pbt), or off (pbf). Not a huge difference between if pencil beams are on or off. 

The plane footprints can drastically lower fO, and not surprisingly decrease the cosmological metrics. 

Transients can get a boost, along with fast microlensing since the bulge often gets more coverage. 

We need some metrics that can measure the science cases in the relevant footprint areas. Right now we have a few science cases that improve, but these footprint changes are large enough that they impact SRD requirements and cosmology metrics fairly quickly.

## Good seeing ##

Getting a lot of scatter on the Transients metric. Not sure how real that is. 

These runs attempted to get 3 "good seeing" observations in (u),g,r,i each season. There are so few u-band observations, it's difficult to increase the area that has good seeing. 

There doesn't seem to be much major science impact on adding the good seeing observations. We need some way to quantify what improves when we do it however. 


## Action Items ##

* SNe group needs to verify that our SNe metric is giving reasonable values (I still suspect an nside bug that is affecting absolute number values, but relative values should be fine). Could also be a difference in "Number of SNe at median z" vs "cumulative SNe to median z".

* Check with transient group about why transient score shows improvement on some of the galactic plane footprints.

* The `roll_early` actually looks pretty good. This would be a good thing to let the rolling cadence team and MWLV fight about

* Seems like we might be able to shave a little bit of time off the NES, good to let the Solar System group weigh in since I only looked at a few of their many metrics. Would be nice to know which metrics are NES sensitive.

* As usual, we ran a lot of things that were requested. We think we did what was asked for, but we don't have any metrics from the community that clearly show an improvement.

* The DESC DDF requests can have very different filter distributions than our previous runs. Are there any other science cases that have filter distribution metrics (photo-z?)





