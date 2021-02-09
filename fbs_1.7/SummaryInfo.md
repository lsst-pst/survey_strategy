## Summary Information 
<a id="top"></a>

In this notebook, we will introduce a series of simulation groups -- the survey strategy simulation families -- and add some additional information describing these families. This includes a description what was changed in the survey strategy variation in that group *and* consolidates some high-level summary statistics from MAF that may aid your analysis of how those survey strategy changes are influencing your metrics. 

* <a href="#List of families">List of families</a>
* <a href="#General overview">General pointers</a>
* <a href="#subnightly timescales">Intranight variations</a>
 * <a href='#visit time'>visit_time (v1.5)</a>
 * <a href="#u long">u_long (v1.7)</a>
 * <a href="#intranight">intranight (v1.5)</a>
 * <a href="#pair_times">pair_times (v1.7)</a>
 * <a href="#twilight_pairs">twilight_pairs (v1.7)</a>
* <a href="#wfd fraction and filters">WFD Fraction and Filter Balance</a>
 * <a href="#wfd_depth">wfd_depth (v1.5)</a>
 * <a href="#filter_dist">filter_dist (v1.5)</a>
* <a href="#footprint options">Survey footprint variations</a><br>
 * <a href="#footprint">footprint (v1.5)</a>
 * <a href="#footprint_tune">footprint_tune (v1.7)</a>
* <a href="#cadence variations">Long timescale cadence variations</a>
 * <a href='#filter_cadence'>filter_cadence (v1.7)</a>
 * <a href="#rolling">rolling (v1.7)</a>
* <a href="#mini-surveys">Mini-mini-survey variations</a>
 * <a href="#twilight_neo">twilight_neo (v1.7)</a>
 * <a href="#shortexp">shortexp (v1.5)</a>
 * <a href="#dcr">dcr (v1.5)</a>
 * <a href="#good_seeing">good_seeing (v1.5)</a>
 * <a href="#spiders">spiders (v1.5)</a>
* <a href="#DDF variations">DDF sequence and dither variations</a>
 * <a href="#ddf">ddf (v1.5)</a>
 * <a href="#ddf_dithers">ddf_dithers (v1.7)</a>
 * <a href="#euclid_dithers">euclid_dithers (v1.7)</a>
* <a href="#potential schedulers">Strategy combinations in 'potential schedulers' (v1.6)</a>
 * <a href="#potential_schedulers">potential_schedulers (v1.6)</a>




```python
# Import our family dictionaries/comments 
# The information in FamilyInfo provides dictionaries to isolate each family group for easier comparison
# A demonstration of more general use of this tool is available at 
# https://github.com/lsst-pst/survey_strategy/blob/master/fbs_1.7/Demo_FamilyInfo.ipynb
import run_infos as ri

families = ri.FamilyInfo()
# Read the summary statistics for all runs
families.read_summary_csv(csv_file='all_summaries_2021_02_09.csv')
```

<a id='List of families'></a>

### List of families 

Which family groups should be considered together and implement a given change in survey strategy?
Note that we have dropped some families from earlier releases and replaced them with updated versions.


```python
family_list = families.list_of_families()
```


**visit_time**, with 3 simulations.<br>**u_long**, with 5 simulations.<br>**intranight**, with 9 simulations.<br>**pair_times**, with 5 simulations.<br>**twilight_pairs**, with 5 simulations.<br>**wfd_depth**, with 17 simulations.<br>**filter_dist**, with 8 simulations.<br>**footprint**, with 19 simulations.<br>**footprint_tune**, with 10 simulations.<br>**filter_cadence**, with 7 simulations.<br>**rolling**, with 25 simulations.<br>**twilight_neo**, with 8 simulations.<br>**shortexp**, with 5 simulations.<br>**dcr**, with 7 simulations.<br>**good_seeing**, with 6 simulations.<br>**spiders**, with 2 simulations.<br>**ddf**, with 4 simulations.<br>**ddf_dithers**, with 8 simulations.<br>**euclid_dithers**, with 5 simulations.<br>**potential_schedulers**, with 17 simulations.<br>


    For 175 simulations in all.


<a id="general overview"></a>

## In general:

Unless otherwise noted: 
* Visits are always 1x30s or 2x15s. For v1.5 and v1.6, the default is 1x30s. For v1.7, the default is 2x15s. The 1x30s simulations achieve about 2.2M visits over 10 years. The 2x15s visits achieve about 2.0M visits. We used 1x30s visits in the earlier simulations but unfortunately are realizing that we absolutely must plan for 2x15s in the overall strategy at this time, so all further simulations will be based on 2x15s visits.
* Pairs of visits in each night are in two filters as follows: u-g, u-r, g-r, r-i, i-z, z-y or y-y. Pairs are scheduled for approximately 22 minutes separation. Almost every visit in gri has another visit within 50 minutes.
* The survey footprint is the standard baseline footprint, with 18K square degrees in the WFD reaching from -62 to +2 degrees (excluding the galactic plane), with additional coverage for the North Ecliptic Spur (NES), the Galactic Plane (GP) and South Celestial Pole (SCP). Five DD fields are included, with the fifth field being composed of two pointings covering the Euclid Deep Field - South (EDF-S), and we allocate 5% of the total survey time to the DD fields. 
* The standard balance of visits between filters is 6% in *u*, 9% in *g*, 22% in *r*, 22% in *i*, 20% in *z*, and 21 % in *y*. 
* *u* band is loaded in and out of the filter holder at 40% lunar illumination (corresponding to approximately new moon +/- 6 nights). 

As a quick way to approach 'decoding' a simulation run name: The name always starts with the family, followed by some encoding of how that particular run has implemented some survey strategy variation, followed by the release version (v1.5 or v1.6 for example), and ending with `_10yrs.db`. 
For example: `goodseeing_i_v1.5_10yrs.db` is from the `good seeing` family and contains at least one visit per year in i band ensured to be acquired in good seeing, and it is from v1.5.
`footprint_gpsmoothv1.5_10yrs.db` is from the `footprint` family in v1.5, and the variation on the survey footprint is that the Galactic Plane is covered at the same depth as the WFD. To decode the particular details of the survey strategy variation, it will likely be necessary to look further at the description of the family in the release notes or in the information below. 

<a id="subnightly timescales"></a> 
<a href="#top">Back to top</a>

## Variations on sub-nightly timescales

<a id='visit time'></a>


```python
families.family_info('visit_time')
```


**visit_time** = simulations bearing on the length of the individual visits. This demonstrates the impact of 1x30s vs. 2x15s visits (9% more visits). The variable exposure run allows the exposure time per visit to vary between 20-100 seconds to attempt to hold the single image visit depth roughly constant, but results in slightly fewer visits overall.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>1x30s</td>
    </tr>
    <tr>
      <th>baseline_2snaps_v1.5_10yrs</th>
      <td>17996.134341</td>
      <td>15087.981860</td>
      <td>892.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>2x15s</td>
    </tr>
    <tr>
      <th>var_expt_v1.5_10yrs</th>
      <td>18576.086249</td>
      <td>15417.824263</td>
      <td>1048.0</td>
      <td>57.0</td>
      <td>82.0</td>
      <td>194.0</td>
      <td>195.0</td>
      <td>172.0</td>
      <td>183.0</td>
      <td>1xVariable</td>
    </tr>
  </tbody>
</table>
</div>



<a id="u long"></a>


```python
families.family_info('u_long')
```


**u_long** = simulations bearing on the length of the u-band exposure time. These simulations swap a single exposure per visit of variable length for each visit in *u* band. The number of *u* band visits is left unchanged, resulting in a shift of visits from other filters to compensate for the increase in time. (Note the DDF visits were left unchanged at 2x15s each).<br>
There is an additional u_long simulation in v1.5 called `u60_v1.5_10yrs`; the u60 v1.5 simulation uses 2x30s u band visits but cuts the number of visits in half rather than maintaining the number of u-band visits as the family below does. Halving u visits was a no-go for transient science (shown in the TDE metric), and so is dropped here. 


    Comparison run: baseline_nexp2_1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>u 2x15s</td>
    </tr>
    <tr>
      <th>u_long_ms_30_v1.7_10yrs</th>
      <td>18091.813816</td>
      <td>15186.179216</td>
      <td>904.0</td>
      <td>58.0</td>
      <td>80.0</td>
      <td>192.0</td>
      <td>193.0</td>
      <td>173.0</td>
      <td>182.0</td>
      <td>u 1x30s</td>
    </tr>
    <tr>
      <th>u_long_ms_40_v1.7_10yrs</th>
      <td>17973.473412</td>
      <td>15118.196431</td>
      <td>889.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>u 1x40s</td>
    </tr>
    <tr>
      <th>u_long_ms_50_v1.7_10yrs</th>
      <td>18138.814260</td>
      <td>15095.535503</td>
      <td>929.0</td>
      <td>53.0</td>
      <td>77.0</td>
      <td>186.0</td>
      <td>187.0</td>
      <td>167.0</td>
      <td>178.0</td>
      <td>u 1x50s</td>
    </tr>
    <tr>
      <th>u_long_ms_60_v1.7_10yrs</th>
      <td>18112.796157</td>
      <td>15011.606138</td>
      <td>915.0</td>
      <td>51.0</td>
      <td>76.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>166.0</td>
      <td>175.0</td>
      <td>u 1x60s</td>
    </tr>
  </tbody>
</table>
</div>



<a id="intranight"></a>


```python
families.family_info('intranight')
```


**intranight** = simulations bearing on the distribution of visits within a night. Snaps per visit (2x15s vs 1x30s) is included for completeness, but the other simulations include variations on whether visits are in the same or mixed filters, and the effect of devoting a fraction of time to obtaining an additional (third) visit per night. <br>
In the `third_obs` simulations, we add a third visit per night to augment the pairs of visits, by adding a *g*, *r*, *i* or *z* visit at the end of the night in the WFD. The amount of the night dedicated to obtaining this third visit at the end of the night varies across the family, from 15 minutes to 120 minutes (corresponding to covering approximately one blob to about five, or half of the night's pairs receiving a third visit). We find the third visit decreases the amount of sky imaged in each night and has an accompanying negative impact on metrics which prefer more sky area within a given time (such as solar system discovery and slower transient metrics, such as SNIa) -- the amount of this impact varies from negligible to noticeable depending on how much time is allocated to the third visit.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_2snaps_v1.5_10yrs</th>
      <td>17996.134341</td>
      <td>15087.981860</td>
      <td>892.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>2x15s visits mixed filters</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>1x30s visits mixed filters</td>
    </tr>
    <tr>
      <th>baseline_samefilt_v1.5_10yrs</th>
      <td>18304.155108</td>
      <td>15317.948319</td>
      <td>1003.0</td>
      <td>71.0</td>
      <td>88.0</td>
      <td>210.0</td>
      <td>210.0</td>
      <td>190.0</td>
      <td>196.0</td>
      <td>1x30s visits same filter</td>
    </tr>
    <tr>
      <th>third_obs_pt15v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>third visits for 15 min</td>
    </tr>
    <tr>
      <th>third_obs_pt30v1.5_10yrs</th>
      <td>18208.475633</td>
      <td>15244.090478</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>206.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>196.0</td>
      <td>third visits for 30 min</td>
    </tr>
    <tr>
      <th>third_obs_pt45v1.5_10yrs</th>
      <td>18222.743625</td>
      <td>15257.519176</td>
      <td>968.0</td>
      <td>59.0</td>
      <td>86.0</td>
      <td>206.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>196.0</td>
      <td>third visits for 45 min</td>
    </tr>
    <tr>
      <th>third_obs_pt60v1.5_10yrs</th>
      <td>18216.029276</td>
      <td>15274.305049</td>
      <td>969.0</td>
      <td>59.0</td>
      <td>87.0</td>
      <td>206.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>196.0</td>
      <td>third visits for 60 min</td>
    </tr>
    <tr>
      <th>third_obs_pt90v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15261.715645</td>
      <td>973.0</td>
      <td>60.0</td>
      <td>87.0</td>
      <td>207.0</td>
      <td>208.0</td>
      <td>186.0</td>
      <td>197.0</td>
      <td>third visits for 90 min</td>
    </tr>
    <tr>
      <th>third_obs_pt120v1.5_10yrs</th>
      <td>18235.333030</td>
      <td>15264.233525</td>
      <td>975.0</td>
      <td>59.0</td>
      <td>87.0</td>
      <td>206.0</td>
      <td>208.0</td>
      <td>186.0</td>
      <td>197.0</td>
      <td>third visits for 120 min</td>
    </tr>
  </tbody>
</table>
</div>



<a id="pair_times"></a>


```python
families.family_info('pair_times')
```


**pair_times** = these simulations explore the impact of varying the time between pairs of visits in a night. Varying the pair time changes the overall number of filter changes per night, so longer pair times result in more visits overall in the survey. Longer pair times are more vulnerable to interruption however, resulting in a lower fraction of visits occuring in pairs. This family is related to the intranight family, but is from v1.7 so must be considered separately. The standard baseline attempts pairs at 22 minutes.


    Comparison run: pair_times_22_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>pair_times_11_v1.7_10yrs</th>
      <td>14356.957095</td>
      <td>15118.196431</td>
      <td>845.0</td>
      <td>51.0</td>
      <td>74.0</td>
      <td>180.0</td>
      <td>181.0</td>
      <td>162.0</td>
      <td>173.0</td>
      <td>11 minute pairs</td>
    </tr>
    <tr>
      <th>pair_times_22_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>22 minute pairs (baseline)</td>
    </tr>
    <tr>
      <th>pair_times_33_v1.7_10yrs</th>
      <td>18076.706531</td>
      <td>15145.893121</td>
      <td>902.0</td>
      <td>57.0</td>
      <td>80.0</td>
      <td>192.0</td>
      <td>192.0</td>
      <td>172.0</td>
      <td>182.0</td>
      <td>33 minute pairs</td>
    </tr>
    <tr>
      <th>pair_times_44_v1.7_10yrs</th>
      <td>18104.403221</td>
      <td>15112.321376</td>
      <td>909.0</td>
      <td>59.0</td>
      <td>81.0</td>
      <td>193.0</td>
      <td>194.0</td>
      <td>173.0</td>
      <td>183.0</td>
      <td>44 minute pairs</td>
    </tr>
    <tr>
      <th>pair_times_55_v1.7_10yrs</th>
      <td>18108.599689</td>
      <td>15072.874574</td>
      <td>913.0</td>
      <td>59.0</td>
      <td>82.0</td>
      <td>194.0</td>
      <td>194.0</td>
      <td>173.0</td>
      <td>183.0</td>
      <td>55 minute pairs</td>
    </tr>
  </tbody>
</table>
</div>



<a id="twilight_pairs"></a>


```python
families.family_info('twilight_pairs')
```


**twilight_pairs** = explore the effect of programming twilight observing in pairs, rather than single visits. The baseline chooses visits during twilight (-18 to -12 degrees solar altitude) one at a time using a greedy algorithm. This family programs visits during twilight in pairs, similarly to the remainder of the night but with a shorter return interval of 15 minutes. In some simulations, visits during morning twilight are preferentially chosen to be areas of the sky already observed earlier in the night. Depending on the simulation, pairs are taken in the same filter (r+r, i+i, z+z, or y+y), or mixed filters (r+i, i+z, z+y or y+y).


    Comparison run: baseline_nexp2_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Baseline (greedy)</td>
    </tr>
    <tr>
      <th>twi_pairs_v1.7_10yrs</th>
      <td>17989.419991</td>
      <td>15220.590256</td>
      <td>892.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>190.0</td>
      <td>191.0</td>
      <td>171.0</td>
      <td>181.0</td>
      <td>Twi pairs same filter</td>
    </tr>
    <tr>
      <th>twi_pairs_mixed_v1.7_10yrs</th>
      <td>17914.722857</td>
      <td>15208.840145</td>
      <td>885.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>192.0</td>
      <td>168.0</td>
      <td>180.0</td>
      <td>Twi pairs mixed filters</td>
    </tr>
    <tr>
      <th>twi_pairs_repeat_v1.7_10yrs</th>
      <td>18001.170102</td>
      <td>15211.358026</td>
      <td>893.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>190.0</td>
      <td>191.0</td>
      <td>171.0</td>
      <td>182.0</td>
      <td>Twi pairs same filter, repeat area</td>
    </tr>
    <tr>
      <th>twi_pairs_mixed_repeat_v1.7_10yrs</th>
      <td>17937.383785</td>
      <td>15215.554494</td>
      <td>886.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>192.0</td>
      <td>168.0</td>
      <td>180.0</td>
      <td>Twi pairs mixed filters, repeat area</td>
    </tr>
  </tbody>
</table>
</div>



<a id="wfd fraction and filters"></a>
<a href="#top">Back to top</a>

## Variations on WFD time and filters 

<a id="wfd_depth"></a>


```python
families.family_info('wfd_depth')
```


**wfd_depth** = evaluates the impact of scaling the fraction of survey time devoted to WFD (and thus the number of visits per pointing in the WFD) up or down. For metrics which respond simply to number of visits, this is a useful family to demonstrate that effect. Metrics which require coverage outside the WFD but are still sensitive to number of visits will show more complicated behavior as coverage in the NES and GP is reduced or increased. When the DDF fields are present, they are allocated 5% of the available survey time.<br>
 From these simulations we determined that between 1.65 and 1.7M visits  are required to cover 18K square degrees of the standard WFD to a minimum number of visits of 825 per pointing; some of the range in that required number of visits comes from over and under subscription in some parts of the sky, which leads to unevenness in coverage. 


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>Baseline</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.65_noddf_v1.5_10yrs</th>
      <td>13596.557052</td>
      <td>15357.395120</td>
      <td>842.0</td>
      <td>56.0</td>
      <td>81.0</td>
      <td>179.0</td>
      <td>180.0</td>
      <td>161.0</td>
      <td>168.0</td>
      <td>65% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.70_noddf_v1.5_10yrs</th>
      <td>18556.782496</td>
      <td>15422.860024</td>
      <td>864.0</td>
      <td>57.0</td>
      <td>83.0</td>
      <td>186.0</td>
      <td>188.0</td>
      <td>168.0</td>
      <td>174.0</td>
      <td>70% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.75_noddf_v1.5_10yrs</th>
      <td>18324.298156</td>
      <td>15448.038834</td>
      <td>899.0</td>
      <td>60.0</td>
      <td>84.0</td>
      <td>195.0</td>
      <td>196.0</td>
      <td>175.0</td>
      <td>182.0</td>
      <td>75% noDDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.80_noddf_v1.5_10yrs</th>
      <td>18268.065482</td>
      <td>15475.735524</td>
      <td>938.0</td>
      <td>60.0</td>
      <td>85.0</td>
      <td>199.0</td>
      <td>200.0</td>
      <td>179.0</td>
      <td>189.0</td>
      <td>80% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.85_noddf_v1.5_10yrs</th>
      <td>18295.762172</td>
      <td>15467.342588</td>
      <td>978.0</td>
      <td>61.0</td>
      <td>88.0</td>
      <td>208.0</td>
      <td>209.0</td>
      <td>187.0</td>
      <td>198.0</td>
      <td>85% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.90_noddf_v1.5_10yrs</th>
      <td>18382.209417</td>
      <td>15309.555382</td>
      <td>1016.0</td>
      <td>63.0</td>
      <td>91.0</td>
      <td>217.0</td>
      <td>217.0</td>
      <td>195.0</td>
      <td>205.0</td>
      <td>90% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.95_noddf_v1.5_10yrs</th>
      <td>18468.656663</td>
      <td>15281.019398</td>
      <td>1057.0</td>
      <td>64.0</td>
      <td>94.0</td>
      <td>226.0</td>
      <td>227.0</td>
      <td>203.0</td>
      <td>214.0</td>
      <td>95% noDDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.99_noddf_v1.5_10yrs</th>
      <td>18514.817813</td>
      <td>15298.644565</td>
      <td>1093.0</td>
      <td>65.0</td>
      <td>97.0</td>
      <td>235.0</td>
      <td>236.0</td>
      <td>210.0</td>
      <td>221.0</td>
      <td>99% no DDF</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.65_v1.5_10yrs</th>
      <td>5629.142478</td>
      <td>15189.536391</td>
      <td>805.0</td>
      <td>54.0</td>
      <td>77.0</td>
      <td>170.0</td>
      <td>171.0</td>
      <td>154.0</td>
      <td>160.0</td>
      <td>65%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.70_v1.5_10yrs</th>
      <td>8996.388583</td>
      <td>15260.037057</td>
      <td>824.0</td>
      <td>56.0</td>
      <td>79.0</td>
      <td>177.0</td>
      <td>179.0</td>
      <td>161.0</td>
      <td>166.0</td>
      <td>70%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.75_v1.5_10yrs</th>
      <td>15800.542165</td>
      <td>15359.073707</td>
      <td>858.0</td>
      <td>57.0</td>
      <td>80.0</td>
      <td>186.0</td>
      <td>186.0</td>
      <td>167.0</td>
      <td>173.0</td>
      <td>75%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.80_v1.5_10yrs</th>
      <td>18049.849134</td>
      <td>15375.020287</td>
      <td>894.0</td>
      <td>58.0</td>
      <td>80.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>80%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.85_v1.5_10yrs</th>
      <td>18173.225300</td>
      <td>15362.430882</td>
      <td>932.0</td>
      <td>59.0</td>
      <td>84.0</td>
      <td>197.0</td>
      <td>199.0</td>
      <td>178.0</td>
      <td>188.0</td>
      <td>85%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.90_v1.5_10yrs</th>
      <td>18222.743625</td>
      <td>15244.929772</td>
      <td>968.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>206.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>196.0</td>
      <td>90%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.95_v1.5_10yrs</th>
      <td>18295.762172</td>
      <td>15226.465311</td>
      <td>1007.0</td>
      <td>61.0</td>
      <td>89.0</td>
      <td>215.0</td>
      <td>216.0</td>
      <td>193.0</td>
      <td>204.0</td>
      <td>95%</td>
    </tr>
    <tr>
      <th>wfd_depth_scale0.99_v1.5_10yrs</th>
      <td>18405.709639</td>
      <td>15245.769065</td>
      <td>1042.0</td>
      <td>62.0</td>
      <td>92.0</td>
      <td>223.0</td>
      <td>224.0</td>
      <td>201.0</td>
      <td>211.0</td>
      <td>99%</td>
    </tr>
  </tbody>
</table>
</div>



<a id='filter_dist'></a>


```python
families.family_info('filter_dist')
```


**filter_dist** = evaluate the impact of changing the balance of visits between filters. Note that this family uses a simplified footprint that is a simple stripe of Declination corresponding to the traditional WFD declination limits but no NES or SCP and continuing WFD over the GP. Generally we find transients and variable stars metrics favor bluer distributions of filters while solar system and galaxy metrics prefer redder distributions of filters (particularly *i* band). 


    Comparison run: filterdist_indx2_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>filterdist_indx1_v1.5_10yrs</th>
      <td>19897.134447</td>
      <td>14304.920889</td>
      <td>1056.0</td>
      <td>164.0</td>
      <td>173.0</td>
      <td>174.0</td>
      <td>175.0</td>
      <td>177.0</td>
      <td>185.0</td>
      <td>Uniform</td>
    </tr>
    <tr>
      <th>filterdist_indx2_v1.5_10yrs</th>
      <td>19907.205971</td>
      <td>15253.322708</td>
      <td>1058.0</td>
      <td>68.0</td>
      <td>99.0</td>
      <td>230.0</td>
      <td>231.0</td>
      <td>207.0</td>
      <td>215.0</td>
      <td>Baseline</td>
    </tr>
    <tr>
      <th>filterdist_indx4_v1.5_10yrs</th>
      <td>19886.223630</td>
      <td>14974.677218</td>
      <td>1057.0</td>
      <td>166.0</td>
      <td>91.0</td>
      <td>206.0</td>
      <td>205.0</td>
      <td>188.0</td>
      <td>195.0</td>
      <td>u heavy</td>
    </tr>
    <tr>
      <th>filterdist_indx3_v1.5_10yrs</th>
      <td>19913.920320</td>
      <td>14922.641012</td>
      <td>1057.0</td>
      <td>65.0</td>
      <td>197.0</td>
      <td>208.0</td>
      <td>203.0</td>
      <td>185.0</td>
      <td>192.0</td>
      <td>g heavy</td>
    </tr>
    <tr>
      <th>filterdist_indx6_v1.5_10yrs</th>
      <td>19918.116788</td>
      <td>15382.573929</td>
      <td>1061.0</td>
      <td>61.0</td>
      <td>89.0</td>
      <td>208.0</td>
      <td>311.0</td>
      <td>189.0</td>
      <td>195.0</td>
      <td>i heavy</td>
    </tr>
    <tr>
      <th>filterdist_indx5_v1.5_10yrs</th>
      <td>19919.795375</td>
      <td>15153.446764</td>
      <td>1061.0</td>
      <td>57.0</td>
      <td>79.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>271.0</td>
      <td>281.0</td>
      <td>z and y heavy</td>
    </tr>
    <tr>
      <th>filterdist_indx7_v1.5_10yrs</th>
      <td>19908.884558</td>
      <td>15126.589368</td>
      <td>1056.0</td>
      <td>99.0</td>
      <td>127.0</td>
      <td>214.0</td>
      <td>214.0</td>
      <td>194.0</td>
      <td>202.0</td>
      <td>Bluer</td>
    </tr>
    <tr>
      <th>filterdist_indx8_v1.5_10yrs</th>
      <td>19908.884558</td>
      <td>15244.929772</td>
      <td>1059.0</td>
      <td>62.0</td>
      <td>90.0</td>
      <td>207.0</td>
      <td>229.0</td>
      <td>227.0</td>
      <td>236.0</td>
      <td>Redder</td>
    </tr>
  </tbody>
</table>
</div>



<a id="footprint options"></a>
<a href="#top">Back to top</a>

## Variations on the survey footprint

<a id="footprint"></a>


```python
families.family_info('footprint')
```


**footprint** = an initial large set of simulations exploring widely different options for the overall survey footprint. The fraction of time devoted to the WFD will necessarily vary among these simulations; this is one of the parameters suitable for later fine-tuning. All runs in this family use 1x30s visits. Some of these footprints contain a traditional WFD footprint, while others contain a shifted/extended N/S footprint that sometimes includes a dust extinction limit around the galactic plane and sometimes a simple galactic latitude cutoff; the bulges family is included because without significant galactic bulge coverage metrics related to MW populations fell significantly, yet the time requirement to cover all of the relevant areas together must be considered.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>filterdist_indx2_v1.5_10yrs</th>
      <td>19907.205971</td>
      <td>15253.322708</td>
      <td>1058.0</td>
      <td>68.0</td>
      <td>99.0</td>
      <td>230.0</td>
      <td>231.0</td>
      <td>207.0</td>
      <td>215.0</td>
      <td>no nes</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>standard baseline</td>
    </tr>
    <tr>
      <th>footprint_standard_goalsv1.5_10yrs</th>
      <td>18205.957752</td>
      <td>15244.090478</td>
      <td>966.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>196.0</td>
      <td>standard baseline again</td>
    </tr>
    <tr>
      <th>footprint_bluer_footprintv1.5_10yrs</th>
      <td>18208.475633</td>
      <td>14954.534170</td>
      <td>967.0</td>
      <td>61.0</td>
      <td>175.0</td>
      <td>206.0</td>
      <td>202.0</td>
      <td>144.0</td>
      <td>151.0</td>
      <td>bluer filters</td>
    </tr>
    <tr>
      <th>footprint_no_gp_northv1.5_10yrs</th>
      <td>18077.545824</td>
      <td>15246.608359</td>
      <td>976.0</td>
      <td>60.0</td>
      <td>87.0</td>
      <td>208.0</td>
      <td>209.0</td>
      <td>187.0</td>
      <td>198.0</td>
      <td>no GP N extension</td>
    </tr>
    <tr>
      <th>footprint_gp_smoothv1.5_10yrs</th>
      <td>20096.886335</td>
      <td>15184.500629</td>
      <td>908.0</td>
      <td>58.0</td>
      <td>82.0</td>
      <td>194.0</td>
      <td>195.0</td>
      <td>174.0</td>
      <td>185.0</td>
      <td>GP at WFD level</td>
    </tr>
    <tr>
      <th>footprint_add_mag_cloudsv1.5_10yrs</th>
      <td>18541.675210</td>
      <td>15408.592032</td>
      <td>953.0</td>
      <td>59.0</td>
      <td>85.0</td>
      <td>203.0</td>
      <td>204.0</td>
      <td>183.0</td>
      <td>194.0</td>
      <td>add MagClouds</td>
    </tr>
    <tr>
      <th>footprint_big_sky_dustv1.5_10yrs</th>
      <td>18038.938317</td>
      <td>17631.880899</td>
      <td>961.0</td>
      <td>56.0</td>
      <td>84.0</td>
      <td>205.0</td>
      <td>206.0</td>
      <td>184.0</td>
      <td>192.0</td>
      <td>big sky, dust-no GP</td>
    </tr>
    <tr>
      <th>footprint_big_skyv1.5_10yrs</th>
      <td>18034.741848</td>
      <td>16730.479524</td>
      <td>1022.0</td>
      <td>65.0</td>
      <td>92.0</td>
      <td>218.0</td>
      <td>219.0</td>
      <td>196.0</td>
      <td>209.0</td>
      <td>big sky - no GP</td>
    </tr>
    <tr>
      <th>footprint_big_sky_nouiyv1.5_10yrs</th>
      <td>18079.224411</td>
      <td>16705.300714</td>
      <td>1045.0</td>
      <td>66.0</td>
      <td>94.0</td>
      <td>223.0</td>
      <td>229.0</td>
      <td>201.0</td>
      <td>214.0</td>
      <td>big sky - no GP, no uiy</td>
    </tr>
    <tr>
      <th>footprint_big_wfdv1.5_10yrs</th>
      <td>2946.759988</td>
      <td>17418.700313</td>
      <td>803.0</td>
      <td>51.0</td>
      <td>72.0</td>
      <td>170.0</td>
      <td>172.0</td>
      <td>153.0</td>
      <td>163.0</td>
      <td>big WFD</td>
    </tr>
    <tr>
      <th>footprint_newAv1.5_10yrs</th>
      <td>443.986338</td>
      <td>17174.465862</td>
      <td>777.0</td>
      <td>49.0</td>
      <td>69.0</td>
      <td>166.0</td>
      <td>166.0</td>
      <td>144.0</td>
      <td>152.0</td>
      <td>big sky + GP1 + NES</td>
    </tr>
    <tr>
      <th>footprint_newBv1.5_10yrs</th>
      <td>14463.547388</td>
      <td>16590.317485</td>
      <td>845.0</td>
      <td>49.0</td>
      <td>72.0</td>
      <td>178.0</td>
      <td>179.0</td>
      <td>155.0</td>
      <td>161.0</td>
      <td>big sky + GP2 + NES</td>
    </tr>
    <tr>
      <th>bulges_bs_v1.5_10yrs</th>
      <td>18866.481851</td>
      <td>17253.359465</td>
      <td>872.0</td>
      <td>54.0</td>
      <td>76.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>164.0</td>
      <td>176.0</td>
      <td>big sky + GP bulge</td>
    </tr>
    <tr>
      <th>bulges_cadence_bs_v1.5_10yrs</th>
      <td>18879.910549</td>
      <td>17239.091473</td>
      <td>872.0</td>
      <td>54.0</td>
      <td>76.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>165.0</td>
      <td>176.0</td>
      <td>big sky + GP bulge cadenced</td>
    </tr>
    <tr>
      <th>bulges_bulge_wfd_v1.5_10yrs</th>
      <td>18225.261506</td>
      <td>17170.269394</td>
      <td>862.0</td>
      <td>54.0</td>
      <td>75.0</td>
      <td>181.0</td>
      <td>182.0</td>
      <td>163.0</td>
      <td>174.0</td>
      <td>big sky + GP bulge @ WFD</td>
    </tr>
    <tr>
      <th>bulges_cadence_bulge_wfd_v1.5_10yrs</th>
      <td>18280.654886</td>
      <td>17320.502956</td>
      <td>862.0</td>
      <td>54.0</td>
      <td>76.0</td>
      <td>181.0</td>
      <td>182.0</td>
      <td>163.0</td>
      <td>174.0</td>
      <td>big sky + GP bulge @WFD cadenced</td>
    </tr>
    <tr>
      <th>bulges_i_heavy_v1.5_10yrs</th>
      <td>18261.351133</td>
      <td>17250.841584</td>
      <td>862.0</td>
      <td>54.0</td>
      <td>75.0</td>
      <td>180.0</td>
      <td>182.0</td>
      <td>162.0</td>
      <td>174.0</td>
      <td>big sky + GP i heavy</td>
    </tr>
    <tr>
      <th>bulges_cadence_i_heavy_v1.5_10yrs</th>
      <td>18270.583363</td>
      <td>17176.144449</td>
      <td>862.0</td>
      <td>54.0</td>
      <td>75.0</td>
      <td>180.0</td>
      <td>182.0</td>
      <td>162.0</td>
      <td>174.0</td>
      <td>big sky + GP i heavy cadenced</td>
    </tr>
  </tbody>
</table>
</div>



<a id="footprint_tune"></a>


```python
families.family_info('footprint_tune')
```


**footprint_tune** = a further exploration of the survey footprint, exploring options for improving the basic setup used in v1.6 in the 'combo_dust' simulation. We feel combo_dust had a lot of promise, as it improved metrics for a wide range of science without impacting metrics (currently avaialable in MAF) dramatically. However, combo_dust had some issues, especially in terms of contingency available in the WFD area (in case of exceptionally bad weather, it could fail SRD, and as it was only one run, it did not offer variations to attempt to improve MWLV or TVS science, for example). This footprint_tune family offers additional variations on the combo_dust (shifted WFD with dust-extinction-limits) simulation. Generally the WFD here is a dust-extinction limited footprint, but with variable N/S limits. We vary the coverage on the remaining sky. Because this is a v1.7 run, it cannot be compared directly with the footprint family above. (they use 2x15s visits, not 1x30s). 


    Comparison run: baseline_nexp2_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Traditional footprint</td>
    </tr>
    <tr>
      <th>footprint_0_v1.710yrs</th>
      <td>15390.966866</td>
      <td>16492.959422</td>
      <td>853.0</td>
      <td>52.0</td>
      <td>72.0</td>
      <td>177.0</td>
      <td>178.0</td>
      <td>163.0</td>
      <td>173.0</td>
      <td>WFD -70.2&lt;dec&lt;7.8 + north ring</td>
    </tr>
    <tr>
      <th>footprint_1_v1.710yrs</th>
      <td>16478.691430</td>
      <td>16503.030946</td>
      <td>861.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>164.0</td>
      <td>175.0</td>
      <td>WFD -70.2&lt;dec&lt;7.8</td>
    </tr>
    <tr>
      <th>footprint_2_v1.710yrs</th>
      <td>16863.927213</td>
      <td>16476.173549</td>
      <td>867.0</td>
      <td>53.0</td>
      <td>76.0</td>
      <td>184.0</td>
      <td>185.0</td>
      <td>166.0</td>
      <td>176.0</td>
      <td>WFD -67.4&lt;dec&lt;8</td>
    </tr>
    <tr>
      <th>footprint_3_v1.710yrs</th>
      <td>16103.527171</td>
      <td>16377.136899</td>
      <td>857.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>182.0</td>
      <td>183.0</td>
      <td>164.0</td>
      <td>174.0</td>
      <td>WFD -67.4&lt;dec8 + 20deg bridge</td>
    </tr>
    <tr>
      <th>footprint_4_v1.710yrs</th>
      <td>17478.290162</td>
      <td>15428.735080</td>
      <td>884.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>187.0</td>
      <td>188.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>WFD -62.5&lt;dec&lt;3.6 +33deg bridge</td>
    </tr>
    <tr>
      <th>footprint_5_v1.710yrs</th>
      <td>16103.527171</td>
      <td>16377.136899</td>
      <td>857.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>182.0</td>
      <td>183.0</td>
      <td>164.0</td>
      <td>174.0</td>
      <td>WFD -67.4&lt;dec&lt;8 + 20deg bridge (like 3)</td>
    </tr>
    <tr>
      <th>footprint_6_v1.710yrs</th>
      <td>16080.866242</td>
      <td>16438.405335</td>
      <td>856.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>182.0</td>
      <td>183.0</td>
      <td>163.0</td>
      <td>174.0</td>
      <td>WFD -67.4&lt;dec&lt;8 + 20deg bridge (south)</td>
    </tr>
    <tr>
      <th>footprint_7_v1.710yrs</th>
      <td>16880.713086</td>
      <td>16601.228302</td>
      <td>871.0</td>
      <td>53.0</td>
      <td>76.0</td>
      <td>184.0</td>
      <td>185.0</td>
      <td>166.0</td>
      <td>177.0</td>
      <td>WFD -70.2&lt;dec&lt;7.8 no ecliptic in galaxy</td>
    </tr>
    <tr>
      <th>footprint_8_v1.710yrs</th>
      <td>15986.026060</td>
      <td>17413.664551</td>
      <td>860.0</td>
      <td>52.0</td>
      <td>74.0</td>
      <td>182.0</td>
      <td>182.0</td>
      <td>163.0</td>
      <td>173.0</td>
      <td>WFD -70.2&lt;dec&lt;7.8 no galactic</td>
    </tr>
  </tbody>
</table>
</div>



<a id="cadence variations"></a>
<a href="#top">Back to top</a>

## Variations on cadence on long timescales

<a id='filter_cadence'></a>


```python
families.family_info('filter_cadence')
```


**filter_cadence** = investigate the impact of reducing the gaps between g band visits over the month, (essentially down-weighting the lunar cycle by adding a requirement that fields receive visits in g band filter throughout each month). In order to avoid 'long gaps' in g band coverage, additional fill-in visits in g are requested in each night; there is a limit to the number of fill-in visits in each night allowed, and these fill-in visits can be requested as contiguous blobs or non-contiguous pointings. The goal is to improve transient discovery for longer timescale transients which require bluer filter coverage (like SN).


    Comparison run: baseline_nexp2_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Baseline</td>
    </tr>
    <tr>
      <th>cadence_drive_gl30v1.7_10yrs</th>
      <td>17905.490627</td>
      <td>15188.697097</td>
      <td>883.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>168.0</td>
      <td>178.0</td>
      <td>Add g, limit 30/night, non-contiguous</td>
    </tr>
    <tr>
      <th>cadence_drive_gl30_gcbv1.7_10yrs</th>
      <td>17954.169658</td>
      <td>15219.750962</td>
      <td>886.0</td>
      <td>54.0</td>
      <td>80.0</td>
      <td>190.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>178.0</td>
      <td>Add g, limit 30/night, contiguous</td>
    </tr>
    <tr>
      <th>cadence_drive_gl100v1.7_10yrs</th>
      <td>17820.721969</td>
      <td>15176.107693</td>
      <td>881.0</td>
      <td>53.0</td>
      <td>83.0</td>
      <td>190.0</td>
      <td>186.0</td>
      <td>167.0</td>
      <td>176.0</td>
      <td>Add g, limit 100/night, non-contiguous</td>
    </tr>
    <tr>
      <th>cadence_drive_gl100_gcbv1.7_10yrs</th>
      <td>17946.616016</td>
      <td>15190.375685</td>
      <td>887.0</td>
      <td>53.0</td>
      <td>85.0</td>
      <td>192.0</td>
      <td>187.0</td>
      <td>167.0</td>
      <td>177.0</td>
      <td>Add g, limit 100/night, contiguous</td>
    </tr>
    <tr>
      <th>cadence_drive_gl200v1.7_10yrs</th>
      <td>17753.578477</td>
      <td>14972.159337</td>
      <td>883.0</td>
      <td>45.0</td>
      <td>116.0</td>
      <td>191.0</td>
      <td>177.0</td>
      <td>158.0</td>
      <td>168.0</td>
      <td>Add g, limit 200/night, non-contiguous</td>
    </tr>
    <tr>
      <th>cadence_drive_gl200_gcbv1.7_10yrs</th>
      <td>17996.973634</td>
      <td>14996.498853</td>
      <td>893.0</td>
      <td>46.0</td>
      <td>115.0</td>
      <td>194.0</td>
      <td>179.0</td>
      <td>160.0</td>
      <td>170.0</td>
      <td>Add g, limit 200/night, contiguous</td>
    </tr>
  </tbody>
</table>
</div>



<a id="rolling"></a>


```python
families.family_info('rolling')
```


**rolling** = Add a rolling cadence, where some parts of the sky receive a higher number of visits during an 'on' season, followed by a lower number of visits during an 'off' season. During the first year and half, and the last year and half (or so), the sky is covered uniformly as normal. This 'intro' and 'outro' allows for better proper motion coverage, and is 1.5 years instead of 1 to allow the entire sky to receive even coverage during that period. This leaves 6 years for 'rolling'; simulations either split the sky into 2 or 3 declination-based regions which are covered either every other season or every third season. Each of the active regions is actually composed of 2 sub-section in the North and South, to spread follow-up requirements over the sky. Some simulations add an every-other nightly modulation between this northern and southern sub-section; some do not although this may happen to some extent due to 'blob' coverage.


    Comparison run: baseline_nexp2_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Baseline</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.2_nslice2_v1.7_10yrs</th>
      <td>17938.223079</td>
      <td>15145.893121</td>
      <td>885.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.2 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.4_nslice2_v1.7_10yrs</th>
      <td>17914.722857</td>
      <td>15134.143010</td>
      <td>885.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.4 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.6_nslice2_v1.7_10yrs</th>
      <td>17945.776722</td>
      <td>15116.517844</td>
      <td>886.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.6 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.8_nslice2_v1.7_10yrs</th>
      <td>17951.651777</td>
      <td>15127.428661</td>
      <td>886.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.8 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.9_nslice2_v1.7_10yrs</th>
      <td>17958.366127</td>
      <td>15063.642344</td>
      <td>887.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.9 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale1.0_nslice2_v1.7_10yrs</th>
      <td>17919.758619</td>
      <td>15079.588924</td>
      <td>887.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>No Modulation, 1.0 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.2_nslice3_v1.7_10yrs</th>
      <td>17909.687095</td>
      <td>15174.429105</td>
      <td>885.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.2 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.4_nslice3_v1.7_10yrs</th>
      <td>17929.830143</td>
      <td>15120.714312</td>
      <td>886.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.4 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.6_nslice3_v1.7_10yrs</th>
      <td>17916.401444</td>
      <td>15133.303717</td>
      <td>886.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.6 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.8_nslice3_v1.7_10yrs</th>
      <td>17925.633674</td>
      <td>15072.035281</td>
      <td>887.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.8 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale0.9_nslice3_v1.7_10yrs</th>
      <td>17940.740960</td>
      <td>15072.874574</td>
      <td>887.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>No Modulation, 0.9 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_nm_scale1.0_nslice3_v1.7_10yrs</th>
      <td>17914.722857</td>
      <td>15082.106804</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>No Modulation, 1.0 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.2_nslice2_v1.7_10yrs</th>
      <td>17904.651333</td>
      <td>15188.697097</td>
      <td>887.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>181.0</td>
      <td>0.2 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.4_nslice2_v1.7_10yrs</th>
      <td>17934.865905</td>
      <td>15173.589812</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.4 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.6_nslice2_v1.7_10yrs</th>
      <td>17910.526389</td>
      <td>15108.124907</td>
      <td>887.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.6 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.8_nslice2_v1.7_10yrs</th>
      <td>17942.419547</td>
      <td>15112.321376</td>
      <td>888.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.8 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.9_nslice2_v1.7_10yrs</th>
      <td>17923.115793</td>
      <td>15066.160225</td>
      <td>888.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.9 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale1.0_nslice2_v1.7_10yrs</th>
      <td>17937.383785</td>
      <td>15091.339035</td>
      <td>888.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>1.0 strength, 2 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.2_nslice3_v1.7_10yrs</th>
      <td>17939.062373</td>
      <td>15155.964645</td>
      <td>886.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.2 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.4_nslice3_v1.7_10yrs</th>
      <td>17932.348024</td>
      <td>15154.286058</td>
      <td>887.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>189.0</td>
      <td>169.0</td>
      <td>181.0</td>
      <td>0.4 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.6_nslice3_v1.7_10yrs</th>
      <td>17936.544492</td>
      <td>15089.660447</td>
      <td>888.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>188.0</td>
      <td>189.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.6 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.8_nslice3_v1.7_10yrs</th>
      <td>17924.794381</td>
      <td>15092.178328</td>
      <td>889.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.8 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale0.9_nslice3_v1.7_10yrs</th>
      <td>17960.884008</td>
      <td>15051.892233</td>
      <td>889.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>0.9 strength, 3 band</td>
    </tr>
    <tr>
      <th>rolling_scale1.0_nslice3_v1.7_10yrs</th>
      <td>17932.348024</td>
      <td>15034.267067</td>
      <td>889.0</td>
      <td>54.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>1.0 strength, 3 band</td>
    </tr>
  </tbody>
</table>
</div>



<a id="mini-surveys"></a>
<a href="#top">Back to top</a>

## Variations adding mini-mini-surveys

<a id="twilight_neo"></a>


```python
families.family_info('twilight_neo')
```


**twilight_neo** = explore the impact of adding a twilight NEO survey, operating on various timescales and thus requiring varying fraction of survey time. These twilight NEO surveys replace the set initially released in  v1.5, improving the twilight NEO mini-survey performance for NEOs by restricting visits to low solar elongations. Twilight NEO visits are 1 second long, in r,i, and z filters.


    Comparison run: baseline_nexp2_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>twi_neo_pattern1_v1.7_10yrs</th>
      <td>344.949688</td>
      <td>14807.657782</td>
      <td>770.0</td>
      <td>50.0</td>
      <td>67.0</td>
      <td>271.0</td>
      <td>273.0</td>
      <td>247.0</td>
      <td>156.0</td>
      <td>On every night</td>
    </tr>
    <tr>
      <th>twi_neo_pattern2_v1.7_10yrs</th>
      <td>10190.703440</td>
      <td>15061.963757</td>
      <td>829.0</td>
      <td>52.0</td>
      <td>73.0</td>
      <td>202.0</td>
      <td>206.0</td>
      <td>180.0</td>
      <td>168.0</td>
      <td>On every other night</td>
    </tr>
    <tr>
      <th>twi_neo_pattern3_v1.7_10yrs</th>
      <td>14904.176552</td>
      <td>15103.928439</td>
      <td>849.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>198.0</td>
      <td>198.0</td>
      <td>177.0</td>
      <td>172.0</td>
      <td>On every third night</td>
    </tr>
    <tr>
      <th>twi_neo_pattern4_v1.7_10yrs</th>
      <td>16471.977081</td>
      <td>15122.392899</td>
      <td>859.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>197.0</td>
      <td>197.5</td>
      <td>177.0</td>
      <td>174.0</td>
      <td>On every fourth night</td>
    </tr>
    <tr>
      <th>twi_neo_pattern5_v1.7_10yrs</th>
      <td>10011.933894</td>
      <td>15063.642344</td>
      <td>828.0</td>
      <td>52.0</td>
      <td>73.0</td>
      <td>204.0</td>
      <td>203.0</td>
      <td>179.0</td>
      <td>168.0</td>
      <td>On for 4 nights, off for 4 nights</td>
    </tr>
    <tr>
      <th>twi_neo_pattern6_v1.7_10yrs</th>
      <td>12067.364031</td>
      <td>15036.784948</td>
      <td>836.0</td>
      <td>52.0</td>
      <td>74.0</td>
      <td>199.0</td>
      <td>200.0</td>
      <td>177.0</td>
      <td>169.0</td>
      <td>On for 3 nights, off for 4 nights</td>
    </tr>
    <tr>
      <th>twi_neo_pattern7_v1.7_10yrs</th>
      <td>14768.210981</td>
      <td>15088.821154</td>
      <td>848.0</td>
      <td>53.0</td>
      <td>75.0</td>
      <td>197.0</td>
      <td>199.0</td>
      <td>176.0</td>
      <td>172.0</td>
      <td>On for 2 nights, off for 4 nights</td>
    </tr>
    <tr>
      <th>baseline_nexp2_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Baseline (none)</td>
    </tr>
  </tbody>
</table>
</div>



<a id="shortexp"></a>


```python
families.family_info('shortexp')
```


**shortexp** = explore the impact of adding 2 or 5 short exposures of 1 or 5 seconds each year (in all 6 filters). The number of visits in the entire survey increases -- but some will be too short to be useful for some science -- the amount of time used for the mini-survey varies in each of these examples, from 0.5% to 5%.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>short_exp_2ns_1expt_v1.5_10yrs</th>
      <td>18170.707419</td>
      <td>15252.483414</td>
      <td>967.0</td>
      <td>69.0</td>
      <td>98.0</td>
      <td>234.0</td>
      <td>236.0</td>
      <td>210.0</td>
      <td>221.0</td>
      <td>2/yr x 1s</td>
    </tr>
    <tr>
      <th>short_exp_2ns_5expt_v1.5_10yrs</th>
      <td>18143.010729</td>
      <td>15248.286946</td>
      <td>951.0</td>
      <td>68.0</td>
      <td>96.0</td>
      <td>230.0</td>
      <td>232.0</td>
      <td>207.0</td>
      <td>218.0</td>
      <td>2/yr x 5s</td>
    </tr>
    <tr>
      <th>short_exp_5ns_1expt_v1.5_10yrs</th>
      <td>18093.492403</td>
      <td>15215.554494</td>
      <td>950.0</td>
      <td>82.0</td>
      <td>113.0</td>
      <td>268.0</td>
      <td>270.0</td>
      <td>241.0</td>
      <td>253.0</td>
      <td>5/yr x 1s</td>
    </tr>
    <tr>
      <th>short_exp_5ns_5expt_v1.5_10yrs</th>
      <td>18045.652666</td>
      <td>15194.572153</td>
      <td>914.0</td>
      <td>80.0</td>
      <td>110.0</td>
      <td>260.0</td>
      <td>262.0</td>
      <td>233.0</td>
      <td>245.0</td>
      <td>5/yr x 5s</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>Baseline (none)</td>
    </tr>
  </tbody>
</table>
</div>



<a id="dcr"></a>


```python
families.family_info('dcr')
```


**dcr** = explore the impact of adding 1 or 2 high-airmass visits in various bandpasses each year, for the purpose of better-measuring differential chromatic refraction (helping with AGN redshifts and the creation of difference image templates). 


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>dcr_nham1_ug_v1.5_10yrs</th>
      <td>18205.957752</td>
      <td>15265.912113</td>
      <td>965.0</td>
      <td>61.0</td>
      <td>87.0</td>
      <td>205.0</td>
      <td>206.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>1/yr in ug</td>
    </tr>
    <tr>
      <th>dcr_nham1_ugr_v1.5_10yrs</th>
      <td>18208.475633</td>
      <td>15228.143899</td>
      <td>967.0</td>
      <td>62.0</td>
      <td>87.0</td>
      <td>206.0</td>
      <td>206.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>1/yr in ugr</td>
    </tr>
    <tr>
      <th>dcr_nham1_ugri_v1.5_10yrs</th>
      <td>18194.207641</td>
      <td>15159.321820</td>
      <td>967.0</td>
      <td>62.0</td>
      <td>87.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>1/yr in ugri</td>
    </tr>
    <tr>
      <th>dcr_nham2_ug_v1.5_10yrs</th>
      <td>18203.439871</td>
      <td>15270.108581</td>
      <td>968.0</td>
      <td>64.0</td>
      <td>87.0</td>
      <td>204.0</td>
      <td>206.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>2/yr in ug</td>
    </tr>
    <tr>
      <th>dcr_nham2_ugr_v1.5_10yrs</th>
      <td>18205.957752</td>
      <td>15214.715200</td>
      <td>968.0</td>
      <td>63.0</td>
      <td>87.0</td>
      <td>206.0</td>
      <td>205.0</td>
      <td>184.0</td>
      <td>194.0</td>
      <td>2/yr in ugr</td>
    </tr>
    <tr>
      <th>dcr_nham2_ugri_v1.5_10yrs</th>
      <td>18205.957752</td>
      <td>15072.874574</td>
      <td>970.0</td>
      <td>63.0</td>
      <td>88.0</td>
      <td>205.0</td>
      <td>208.0</td>
      <td>183.0</td>
      <td>195.0</td>
      <td>2/yr in ugri</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>Baseline (none)</td>
    </tr>
  </tbody>
</table>
</div>



<a id="good_seeing"></a>


```python
families.family_info('good_seeing')
```


**good_seeing** = explore the effect of prioritizing achieving at least 1 'good seeing' image in the specified bandpasses in each year. These simulations do improve the seeing distributions in the targeted bands, compared to baseline -- this improvement is most visible when comparing the achieved IQ against the standard baseline, within a given year. 


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>goodseeing_i_v1.5_10yrs</th>
      <td>18214.350688</td>
      <td>15387.609691</td>
      <td>966.0</td>
      <td>59.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>208.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>good i band</td>
    </tr>
    <tr>
      <th>goodseeing_gi_v1.5_10yrs</th>
      <td>18216.029276</td>
      <td>15261.715645</td>
      <td>966.0</td>
      <td>59.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>good gi bands</td>
    </tr>
    <tr>
      <th>goodseeing_gz_v1.5_10yrs</th>
      <td>18204.279165</td>
      <td>15255.001295</td>
      <td>965.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>206.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>good gz bands</td>
    </tr>
    <tr>
      <th>goodseeing_gri_v1.5_10yrs</th>
      <td>18215.189982</td>
      <td>15258.358470</td>
      <td>966.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>184.0</td>
      <td>195.0</td>
      <td>good gri bands</td>
    </tr>
    <tr>
      <th>goodseeing_griz_v1.5_10yrs</th>
      <td>18207.636339</td>
      <td>15222.268843</td>
      <td>964.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>206.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>good griz bands</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>baseline - none</td>
    </tr>
  </tbody>
</table>
</div>



<a id="spiders"></a>


```python
families.family_info('spiders')
```


**spiders** = This example simulation explores rotating the camera so that diffraction spikes are aligned with the X/Y directions of the CCD, to reduce artifacts in difference imaging.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>spiders_v1.5_10yrs</th>
      <td>18221.904331</td>
      <td>15244.929772</td>
      <td>969.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>206.0</td>
      <td>207.0</td>
      <td>186.0</td>
      <td>196.0</td>
      <td>Spiders Aligned</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>Random orientation</td>
    </tr>
  </tbody>
</table>
</div>



<a id="DDF variations"></a>
<a href="#top">Back to top</a>

## Variations on the DDFs

<a id="ddf"></a>


```python
families.family_info('ddf')
```


**ddf** = Vary the sequences for DDF fields. The amount of time per DDF field varies between some of these simulations.


    Comparison run: baseline_v1.5_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>agnddf_v1.5_10yrs</th>
      <td>18200.082696</td>
      <td>15261.715645</td>
      <td>960.0</td>
      <td>61.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>205.0</td>
      <td>183.0</td>
      <td>193.0</td>
      <td>AGN sequences</td>
    </tr>
    <tr>
      <th>descddf_v1.5_10yrs</th>
      <td>18183.296823</td>
      <td>15235.697542</td>
      <td>952.0</td>
      <td>59.0</td>
      <td>85.0</td>
      <td>203.0</td>
      <td>203.0</td>
      <td>182.0</td>
      <td>192.0</td>
      <td>DESC sequences</td>
    </tr>
    <tr>
      <th>daily_ddf_v1.5_10yrs</th>
      <td>18143.850022</td>
      <td>15181.143455</td>
      <td>920.0</td>
      <td>57.0</td>
      <td>82.0</td>
      <td>196.0</td>
      <td>197.0</td>
      <td>175.0</td>
      <td>186.0</td>
      <td>Daily sequences</td>
    </tr>
    <tr>
      <th>baseline_v1.5_10yrs</th>
      <td>18217.707863</td>
      <td>15236.536835</td>
      <td>967.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>205.0</td>
      <td>207.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>Baseline</td>
    </tr>
  </tbody>
</table>
</div>



<a id="ddf_dithers"></a>


```python
families.family_info('ddf_dithers')
```


**ddf_dithers** = Vary the translational dither offsets in the DDFs, from 0 to 2.0 degrees. Smaller dithers will help the overall depth and uniformity, but larger dithers may be needed for calibration.


    Comparison run: ddf_dither0.70_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ddf_dither0.00_v1.7_10yrs</th>
      <td>17978.509174</td>
      <td>15155.125352</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0 dither</td>
    </tr>
    <tr>
      <th>ddf_dither0.05_v1.7_10yrs</th>
      <td>17975.151999</td>
      <td>15146.732415</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.05 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither0.10_v1.7_10yrs</th>
      <td>17989.419991</td>
      <td>15163.518288</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.10 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither0.30_v1.7_10yrs</th>
      <td>17964.241182</td>
      <td>15162.678994</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.30 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither0.70_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>0.70 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither1.00_v1.7_10yrs</th>
      <td>17967.598357</td>
      <td>15178.625574</td>
      <td>889.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>1.00 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither1.50_v1.7_10yrs</th>
      <td>17976.830587</td>
      <td>15172.750518</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>1.50 deg dither</td>
    </tr>
    <tr>
      <th>ddf_dither2.00_v1.7_10yrs</th>
      <td>17975.991293</td>
      <td>15184.500629</td>
      <td>889.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>2.00 deg dither</td>
    </tr>
  </tbody>
</table>
</div>



<a id="euclid_dithers"></a>


```python
families.family_info('euclid_dithers')
```


**euclid_dithers** = vary the translational dither offsets to fill in the Euclid DDF footprint, as the Euclid field is a double pointing for Rubin. These simulation vary the spatial dither both towards the second pointing and perpendicular to the second pointing. The perpendicular dithering is relatively small (and symmetric 'up' and 'down'). The dithering along the footprint ('direct') is larger and non-symmetric, with a smaller dither 'away' from the second pointing and a larger dither 'toward' the second pointing. (offsets are in degrees).


    Comparison run: euclid_dither1_v1.7_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>euclid_dither1_v1.7_10yrs</th>
      <td>17982.705642</td>
      <td>15174.429105</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Direct -0.25/+1.0, Perp +/-0.25 (deg)</td>
    </tr>
    <tr>
      <th>euclid_dither2_v1.7_10yrs</th>
      <td>17970.116238</td>
      <td>15192.054272</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Direct -0.1/+1.0, Perp +/-0.25 (deg)</td>
    </tr>
    <tr>
      <th>euclid_dither3_v1.7_10yrs</th>
      <td>17967.598357</td>
      <td>15161.839701</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Direct -0.25/+1.0, Perp +/-0.10 (deg)</td>
    </tr>
    <tr>
      <th>euclid_dither4_v1.7_10yrs</th>
      <td>18012.080920</td>
      <td>15189.536391</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Direct -0.25/+1.5, Perp +/-0.25 (deg)</td>
    </tr>
    <tr>
      <th>euclid_dither5_v1.7_10yrs</th>
      <td>17980.187761</td>
      <td>15170.232637</td>
      <td>888.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>189.0</td>
      <td>190.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Direct -0.25/+0.75, Perp +/-0.25 (deg</td>
    </tr>
  </tbody>
</table>
</div>



<a id="potential schedulers"></a>
<a href="#top">Back to top</a>

## Examples of combinations of survey strategy variations

<a id="potential_schedulers"></a>


```python
families.family_info('potential_schedulers')
```


**potential_schedulers** = A series of simulations where we vary *multiple* survey strategies at once, trying to combine the survey strategies that seemed useful to us (at the time anyway) to reach a particular science goal. These simulations are like cross-sections of the families, using bits and pieces to try to reach goals, rather than explore the impact of the various survey strategy changes individually. Each simulation is repeated for 2x15s visits and for 1x30s visits. <br>
The point here is to illustrate the effect of combinations of survey strategy variations; some are successful and sometimes we may meet technical goals but not science goals. For further details on each simulation, Section 5 in the cadence report for the SCOC (https://pstn-051.lsst.io/) is recommended. 


    Comparison run: baseline_nexp1_v1.6_10yrs





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Area with &gt;825 visits/pointing</th>
      <th>Unextincted area i&gt;25.9</th>
      <th>Median Nvisits over best 18k</th>
      <th>Median Nvis u band</th>
      <th>Median Nvis g band</th>
      <th>Median Nvis r band</th>
      <th>Median Nvis i band</th>
      <th>Median Nvis z band</th>
      <th>Median Nvis y band</th>
      <th>Briefly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>barebones_nexp2_v1.6_10yrs</th>
      <td>18405.709639</td>
      <td>15279.340811</td>
      <td>1067.0</td>
      <td>68.0</td>
      <td>100.0</td>
      <td>232.0</td>
      <td>233.0</td>
      <td>211.0</td>
      <td>213.0</td>
      <td>WFD only 2x15s</td>
    </tr>
    <tr>
      <th>barebones_v1.6_10yrs</th>
      <td>18518.174988</td>
      <td>15328.019842</td>
      <td>1155.0</td>
      <td>74.0</td>
      <td>109.0</td>
      <td>251.0</td>
      <td>252.0</td>
      <td>228.0</td>
      <td>230.0</td>
      <td>WFD only 1x30s</td>
    </tr>
    <tr>
      <th>baseline_nexp2_scaleddown_v1.6_10yrs</th>
      <td>18138.814260</td>
      <td>15187.857804</td>
      <td>925.0</td>
      <td>56.0</td>
      <td>81.0</td>
      <td>197.0</td>
      <td>198.0</td>
      <td>178.0</td>
      <td>188.0</td>
      <td>Baseline 2x15s adjusted WFD fraction</td>
    </tr>
    <tr>
      <th>baseline_nexp2_v1.6_10yrs</th>
      <td>18044.813372</td>
      <td>15169.393344</td>
      <td>897.0</td>
      <td>55.0</td>
      <td>79.0</td>
      <td>191.0</td>
      <td>191.0</td>
      <td>172.0</td>
      <td>182.0</td>
      <td>Baseline 2x15s</td>
    </tr>
    <tr>
      <th>baseline_nexp1_v1.6_10yrs</th>
      <td>18210.154220</td>
      <td>15328.859136</td>
      <td>972.0</td>
      <td>60.0</td>
      <td>86.0</td>
      <td>207.0</td>
      <td>208.0</td>
      <td>186.0</td>
      <td>197.0</td>
      <td>Baseline 1x30s</td>
    </tr>
    <tr>
      <th>combo_dust_nexp2_v1.6_10yrs</th>
      <td>7022.369929</td>
      <td>17063.679101</td>
      <td>817.0</td>
      <td>50.0</td>
      <td>70.0</td>
      <td>171.0</td>
      <td>172.0</td>
      <td>156.0</td>
      <td>166.0</td>
      <td>Combo dust 2x15s</td>
    </tr>
    <tr>
      <th>combo_dust_v1.6_10yrs</th>
      <td>19157.716746</td>
      <td>17702.381565</td>
      <td>885.0</td>
      <td>53.0</td>
      <td>76.0</td>
      <td>186.0</td>
      <td>187.0</td>
      <td>170.0</td>
      <td>180.0</td>
      <td>Combo dust 1x30s</td>
    </tr>
    <tr>
      <th>ddf_heavy_nexp2_v1.6_10yrs</th>
      <td>5404.211782</td>
      <td>14769.889568</td>
      <td>810.0</td>
      <td>50.0</td>
      <td>70.0</td>
      <td>171.0</td>
      <td>173.0</td>
      <td>155.0</td>
      <td>165.0</td>
      <td>DDF 13.4 % 2x15s</td>
    </tr>
    <tr>
      <th>ddf_heavy_v1.6_10yrs</th>
      <td>17677.202755</td>
      <td>15094.696209</td>
      <td>881.0</td>
      <td>54.0</td>
      <td>77.0</td>
      <td>187.0</td>
      <td>188.0</td>
      <td>169.0</td>
      <td>179.0</td>
      <td>DDF 13.4% 1x30s</td>
    </tr>
    <tr>
      <th>dm_heavy_nexp2_v1.6_10yrs</th>
      <td>18076.706531</td>
      <td>15146.732415</td>
      <td>899.0</td>
      <td>58.0</td>
      <td>80.0</td>
      <td>192.0</td>
      <td>191.0</td>
      <td>170.0</td>
      <td>181.0</td>
      <td>DM heavy 2x15s</td>
    </tr>
    <tr>
      <th>dm_heavy_v1.6_10yrs</th>
      <td>18217.707863</td>
      <td>15322.984081</td>
      <td>974.0</td>
      <td>63.0</td>
      <td>88.0</td>
      <td>208.0</td>
      <td>208.0</td>
      <td>185.0</td>
      <td>195.0</td>
      <td>DM heavy 1x30s</td>
    </tr>
    <tr>
      <th>mw_heavy_nexp2_v1.6_10yrs</th>
      <td>18283.172767</td>
      <td>15337.252073</td>
      <td>876.0</td>
      <td>55.0</td>
      <td>78.0</td>
      <td>186.0</td>
      <td>187.0</td>
      <td>168.0</td>
      <td>178.0</td>
      <td>Bulge/MC @ WFD 2x15s</td>
    </tr>
    <tr>
      <th>mw_heavy_v1.6_10yrs</th>
      <td>18881.589136</td>
      <td>15556.307714</td>
      <td>948.0</td>
      <td>59.0</td>
      <td>84.0</td>
      <td>202.0</td>
      <td>203.0</td>
      <td>182.0</td>
      <td>192.0</td>
      <td>Bulge/MC @ WFD 1x30s</td>
    </tr>
    <tr>
      <th>rolling_exgal_mod2_dust_sdf_0.80_nexp2_v1.6_10yrs</th>
      <td>16506.388120</td>
      <td>17211.394782</td>
      <td>865.0</td>
      <td>52.0</td>
      <td>75.0</td>
      <td>183.0</td>
      <td>184.0</td>
      <td>164.0</td>
      <td>174.0</td>
      <td>Shifted rolling WFD 2x15s</td>
    </tr>
    <tr>
      <th>rolling_exgal_mod2_dust_sdf_0.80_v1.6_10yrs</th>
      <td>18006.205864</td>
      <td>17783.793048</td>
      <td>937.0</td>
      <td>55.0</td>
      <td>82.0</td>
      <td>198.0</td>
      <td>199.0</td>
      <td>178.0</td>
      <td>189.0</td>
      <td>Shifted rolling WFD 1x30s</td>
    </tr>
    <tr>
      <th>ss_heavy_nexp2_v1.6_10yrs</th>
      <td>13526.056386</td>
      <td>14694.353140</td>
      <td>840.0</td>
      <td>57.0</td>
      <td>71.0</td>
      <td>266.0</td>
      <td>176.0</td>
      <td>162.0</td>
      <td>169.0</td>
      <td>Twilight pairs + NEO 2x15s</td>
    </tr>
    <tr>
      <th>ss_heavy_v1.6_10yrs</th>
      <td>19109.037714</td>
      <td>15069.517400</td>
      <td>911.0</td>
      <td>61.0</td>
      <td>78.0</td>
      <td>270.0</td>
      <td>190.0</td>
      <td>176.0</td>
      <td>183.0</td>
      <td>Twilight pairs + NEO 1x30s</td>
    </tr>
  </tbody>
</table>
</div>




```python
!jupyter nbconvert --to html SummaryInfo.ipynb
```

    [NbConvertApp] Converting notebook SummaryInfo.ipynb to html
    [NbConvertApp] Writing 694246 bytes to SummaryInfo.html



```python

```
