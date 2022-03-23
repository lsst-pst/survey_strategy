# Notes on the v2.0 and v2.1 runs

## Baseline-like Runs ##

* New baseline includes rolling, which gives a substantial boost to SNe

* New baseline has increased bulge coverage, boosting microlensing

* The new footprint results in 4% decrease in fO metric


## Bluer ##

XXX--what was this trying to do again?

I think this was supposed to give a boost to SNe, but it looks pretty small. Seems to hurt Transients and WL.

## Long u-band exposures ##

Taking longer u-band exposures.  

* Both give a small boost to fO

* long_u1 hurts lots of science metrics, especially SNe and fast microlensing

* long_u2 is mostly neutral, but no obvious gains anywhere

## Rolling experiments ##

We test rolling with different fractions of the sky (half, third, sixth), and two different strenths (50% and 90%). 
Our baseline of half sky at 80-90% seems fairly close to ideal. Rolling with smaller area can boost SNe and TDE metrics, but at significant penalty for proper motions and faint NEOs.

Turning off rolling gives a modest boost to astrometry metrics, but is very bad for almost all transients. 

The `roll_early` tests the impact of adding an additional rolling season. This gives a nice boost to SNe and transients, with a small impact on proper motions. I guess I can point out that if the survey extends slightly, that proper motion precision can be recovered, but once the transients are gone, they are gone forever.

Adding rolling in the bulge doesn't have any perks. We might need more bulge-specific transient metrics.


## Long Gaps ##

The long gaps runs are a pretty clear trade off between the Transients metric and just about everything else. Also an odd effect that the Transients metric seems to get worse when the long gaps are off for 3 or more nights. The increase in the Transients metric seems fairly modest, it's tough to judge since it it a unitless score that increases from 180 to 190-195.

Taking long gaps with no initial pairs seems like a major loss across the board. 

## Presto ##




## Varied galactic plane weight ##

## Varied NES ##



## DDF ##

The new DDF experiments 

We still need more DDF metrics. The QSO one we are running now is depth-only, doesn't seem to have any cadence sensitivity.

* For all the DDF-centric experiements, the final depths and number of visits are all comperable, typically plus/minus 0.1 mags. Can be outliers if the dither size is very large.

* Early pass with the AGN structure function uncertainty doesn't show much difference between runs. May need to tune kwarg parameters (e.g., what magnitude AGN should we be considering?)?

* Doing shorter DDF sequences more often can boost the SNe metrics considerably, but it does result in a lower open shutter fraction because it adds more filter changes. Might be worth looking at observing daily, but only in 2-3 filters rather than all 5. That could maybe maintain the SNe improvement but recover much of the open shutter fraction. 


## Pencil Surveys ##

The `pencil_fs2` run boosts the trainsient metric, but has a fairly significant impact on fO and SNe. The open shutter fraction is down to 68%. This is from not enforcing contiguous blobs. 

The `pencil_fs1` run suffers from the scheduler not being able to easily conenct some of the desired pencil beam areas with other parts of the survey. Currently no metrics show a siginificant improvement over the baseline. The open shutter fraction drops all the way down to 67%. 

If there's a compelling metric that shows improvement with these runs, we can work on extending the scheduler to selectively enforce contiguous blobs and recover most of the lost open shutter fraction. 

## Plane Priority ##

Run with pencil beam surveys on (pbt), or off (pbf). Not a huge difference between if pencil beams are on or off. 

The plane footprints can drastically lower fO, and not surprisingly decrease the cosmological metrics. 

Transients can get a boost, along with fast microlensing since the bulge often gets more coverage. 

We need some metrics that can measure the science cases in the relevant footprint areas. Right now we have a few science cases taht improve, but these footprint changes are large enough that they impact SRD requirements and cosmology metrics fairly quickly.

## Good seeing ##

Getting a lot of scatter on the Transients metric. Not sure how real that is. 

These runs attempted to get 3 "good seeing" observations in (u),g,r,i each season. There are so few u-band observations, it's difficult to increase the area that has good seeing. 

There doesn't seem to be much major science impact on adding the good seeing observations. We need some way to quantify what improves when we do it however. 


## Action Items ##

* SNe group needs to verify that our SNe metric is giving reasonable values (I still suspect an nside bug that is affecting absolute values, but relative values should be fine)

* Check with transient group about why transient score shows improvement on some of the galactic plane footprints.

* The `roll_early` actually looks pretty good. This would be a good thing to let the rolling cadence team and MWLV fight about

