# This file is intended to provide some "reference information" in a useful form for python.
# The names of each run in a family (as defined in the families described in the simulation releases)
# are provided in a dictionary; their most-likely most-relevant comparison run is included as well.
# The file also provides some additional dictionaries, which may group together given families that
# touch on very related points; an example is the 'intranight' family, which includes some simulations
# looking at exposure time within a visit as well as whether to add a third visit - all of these relate
# to the survey strategy within a night.
# Each grouping or family only includes runs from a single release, that can use a single comparison run.
# Data / dictionaries containing the family information include:
# family  - comment - nicknames - family_baseline - family_version

# Much of the text in this file is intended to be used in jupyter notebooks and thus is markdown.

import numpy as np
import pandas as pd
from IPython.display import display_markdown
import matplotlib.pyplot as plt

### METRICS FOR SHORT DISPLAY
tablemetrics = ['fOArea fO All visits HealpixSlicer',
                'Effective Area (deg) ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                # 'Nstars_no_crowding  y HealpixSlicer',
                'Nvisits All',
                'fONv MedianNvis fO All visits HealpixSlicer',
                'Median NVisits u band HealpixSlicer',
                'Median NVisits g band HealpixSlicer',
                'Median NVisits r band HealpixSlicer',
                'Median NVisits i band HealpixSlicer',
                'Median NVisits z band HealpixSlicer',
                'Median NVisits y band HealpixSlicer', ]
tablenames = ['Area with >825 visits/pointing',
              'Unextincted area i>25.9',
              # 'Nstars y band (no crowding)',
              'Nvisits total',
              'Median Nvisits over best 18k',
              'Median Nvis u band',
              'Median Nvis g band',
              'Median Nvis r band',
              'Median Nvis i band',
              'Median Nvis z band',
              'Median Nvis y band']


class FamilyInfo():
    """A class to hold some high-level documentation of the available simulation runs.
    (making this a class rather than just a file just makes it a little clearer to use in a notebook).
    """

    def __init__(self):
        """Where we set all the run information."""
        # Currently relevant runs from these releases will be included below
        self.sim_versions = ['1.5', '1.6', '1.7']

        # Overall baseline runs in each release.
        self.baselines_versions = {'1.5': 'baseline_v1.5_10yrs',  # 1x30s visits
                                   '1.6': 'baseline_nexp2_v1.6_10yrs',  # 2x15s visits
                                   '1.7': 'baseline_nexp2_v1.7_10yrs'  # 2x15s visits
                                   }

        # The simulations included in the survey strategy grouping
        self.family = {}
        # An overall comment about the grouping
        self.comment = {}
        # Potentially useful nicknames or overwhelmingly brief descriptors -- USE THESE SPARINGLY
        # By using the nickname instead of the full name, you lose traceability for which run is really which.
        self.nicknames = {}
        # What is the most-useful comparison run for this grouping
        self.family_baseline = {}
        # The release number for this grouping
        self.family_version = {}

        # Release notes for each of the 1.5, 1.6  and 1.7 families:
        # https://community.lsst.org/t/fbs-1-5-release-may-update-bonus-fbs-1-5-release/
        # https://community.lsst.org/t/fbs-1-6-release-august-2020/
        # https://community.lsst.org/t/survey-simulations-v1-7-release-january-2021/

        # baselines -- this particular 'family' needs to be used differently than the rest.
        key = 'version_baselines'
        c = f"**{key}** = Comparison baselines across each release. The major differences across 1.5, 1.6 to " \
            f"1.7 is whether we decide the default baseline for the release is 2x15s or 1x30s; however, " \
            f"in each release we have created both a 2x15s and a 1x30s baseline -- so any subtle " \
            f"changes due to updates in the telescope model or scheduler code can be evaluated by " \
            f"looking at the same baseline versions. The trickier part of evaluating these at the " \
            f"same time is that the results are likely contained in different dataframes in python " \
            f"(if the big_1.5.csv, big_1.6.csv and big_1.7.csv files were used)."
        self.comment[key] = c
        self.family[key] = ['baseline_2snaps_v1.5_10yrs',
                            'baseline_v1.5_10yrs',
                            'baseline_nexp2_v1.6_10yrs',
                            'baseline_nexp1_v1.6_10yrs',
                            'baseline_nexp2_v1.7_10yrs',
                            'baseline_nexp1_v1.7_10yrs']
        self.nicknames[key] = ['Baseline 2x15s v1.5',
                               'Baseline 1x30s v1.5',
                               'Baseline 2x15s v1.6',
                               'Baseline 1x30s v1.6',
                               'Baseline 2x15 v1.7',
                               'Baseline 1x30s v1.7']
        self.family_baseline[key] = 'baseline_nexp1_v1.7_10yrs'
        self.family_version[key] = 'All'

        ### visit_time
        key = 'visit_time'
        c = f"**{key}** = simulations bearing on the length of the individual visits. " \
            "This demonstrates the impact of 1x30s vs. 2x15s visits (9% more visits). " \
            "The variable exposure run allows the exposure time per visit to vary " \
            "between 20-100 seconds to attempt to hold the single image visit depth roughly constant, " \
            "but results in slightly fewer visits overall (although more visits per pointing within the WFD)."
        self.comment[key] = c
        self.family[key] = ['baseline_v1.5_10yrs',
                            'baseline_2snaps_v1.5_10yrs',
                            'var_expt_v1.5_10yrs']
        self.nicknames[key] = ['1x30s',
                               '2x15s',
                               '1xVariable']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ### u_long
        key = 'u_long'
        c = f"**{key}** = simulations bearing on the length of the u-band exposure time. " \
            f"These simulations swap a single exposure per visit of variable length for each visit in *u* " \
            f"band. The number of *u* band visits is left unchanged, resulting in a shift of visits from " \
            f"other filters to compensate for the increase in time. (Note the DDF visits were left " \
            f"unchanged at 2x15s each)." \
            f"<br>\n" \
            "There is an additional u_long simulation in v1.5 called `u60_v1.5_10yrs`; " \
            "the u60 v1.5 simulation uses 2x30s u band visits but cuts the number of visits in half " \
            "rather than maintaining the number of u-band visits as the family below does. " \
            "Halving u visits was a no-go for transient science (shown in the TDE metric), and so is " \
            "dropped here. "
        self.comment[key] = c
        self.family[key] = ['baseline_nexp2_v1.7_10yrs',
                            'u_long_ms_30_v1.7_10yrs',
                            'u_long_ms_40_v1.7_10yrs',
                            'u_long_ms_50_v1.7_10yrs',
                            'u_long_ms_60_v1.7_10yrs']
        self.nicknames[key] = ['u 2x15s',
                               'u 1x30s',
                               'u 1x40s',
                               'u 1x50s',
                               'u 1x60s']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ## intranight
        key = 'intranight'
        c = f"**{key}** = simulations bearing on the distribution of visits within a night. " \
            "Snaps per visit (2x15s vs 1x30s) is included for completeness, but the other " \
            "simulations include variations on whether visits are in the same or mixed filters, " \
            "and the effect of devoting a fraction of time to obtaining an additional (third) visit " \
            "per night. " \
            "<br>\n" \
            "In the `third_obs` simulations, we add a third visit per night to augment the pairs of " \
            "visits, by adding a *g*, *r*, *i* or *z* visit at the end of the night in the WFD. The " \
            "amount of the night dedicated to obtaining this third visit at the end of the night varies " \
            "across the family, from 15 minutes to 120 minutes (corresponding to covering approximately " \
            "one blob to about five, or half of the night's pairs receiving a third visit). We find " \
            "the third visit decreases the amount of sky imaged in each night and has an accompanying " \
            "negative impact on metrics which prefer more sky area within a given time (such as solar " \
            "system discovery and slower transient metrics, such as SNIa) -- the amount of this " \
            "impact varies from negligible to noticeable depending on how much time is allocated " \
            "to the third visit."
        self.comment[key] = c
        self.family[key] = ['baseline_2snaps_v1.5_10yrs',
                            'baseline_v1.5_10yrs',
                            'baseline_samefilt_v1.5_10yrs',
                            'third_obs_pt15v1.5_10yrs',
                            'third_obs_pt30v1.5_10yrs',
                            'third_obs_pt45v1.5_10yrs',
                            'third_obs_pt60v1.5_10yrs',
                            'third_obs_pt90v1.5_10yrs',
                            'third_obs_pt120v1.5_10yrs']
        self.nicknames[key] = ['2x15s visits mixed filters',
                               '1x30s visits mixed filters',
                               '1x30s visits same filter',
                               'third visits for 15 min',
                               'third visits for 30 min',
                               'third visits for 45 min',
                               'third visits for 60 min',
                               'third visits for 90 min',
                               'third visits for 120 min']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## pair_times
        key = 'pair_times'
        c = f"**{key}** = these simulations explore the impact of varying the time between pairs of visits " \
            f"in a night. Varying the pair time changes the overall number of filter changes per night, " \
            f"so longer pair times result in more visits overall in the survey. Longer pair times are more " \
            f"vulnerable to interruption however, resulting in a lower fraction of visits occuring in pairs. " \
            f"This family is related to the intranight family, but is from v1.7 so must be considered " \
            f"separately. The standard baseline attempts pairs at 22 minutes."
        self.comment[key] = c
        self.family[key] = ['pair_times_11_v1.7_10yrs',
                            'pair_times_22_v1.7_10yrs',
                            'pair_times_33_v1.7_10yrs',
                            'pair_times_44_v1.7_10yrs',
                            'pair_times_55_v1.7_10yrs',
                            'baseline_nexp2_v1.7_10yrs']
        self.nicknames[key] = ['11 minute pairs',
                               '22 minute pairs (baseline)',
                               '33 minute pairs',
                               '44 minute pairs',
                               '55 minute pairs',
                               'Baseline']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ## twilight pairs
        key = 'twilight_pairs'
        c = f"**{key}** = explore the effect of programming twilight observing in pairs, rather than " \
            f"single visits. The baseline chooses visits during twilight (-18 to -12 degrees solar " \
            f"altitude) one at a time using a greedy algorithm. This family programs visits during " \
            f"twilight in pairs, similarly to the remainder of the night but with a shorter return " \
            f"interval of 15 minutes. In some simulations, visits during morning twilight are " \
            f"preferentially chosen to be areas of the sky already observed earlier in the night. " \
            f"Depending on the simulation, pairs are taken in the same filter (r+r, i+i, z+z, or y+y), " \
            f"or mixed filters (r+i, i+z, z+y or y+y)."
        self.comment[key] = c
        self.family[key] = ['baseline_nexp2_v1.7_10yrs',
                            'twi_pairs_v1.7_10yrs',
                            'twi_pairs_mixed_v1.7_10yrs',
                            'twi_pairs_repeat_v1.7_10yrs',
                            'twi_pairs_mixed_repeat_v1.7_10yrs',
                            ]
        self.nicknames[key] = ['Baseline (greedy)',
                               'Twi pairs same filter',
                               'Twi pairs mixed filters',
                               'Twi pairs same filter, repeat area',
                               'Twi pairs mixed filters, repeat area']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ## wfddepth
        key = 'wfd_depth'
        c = f"**{key}** = evaluates the impact of scaling the fraction of survey time devoted to WFD (and thus " \
            f"the number of visits per pointing in the WFD) up or down. For metrics which respond simply " \
            f"to number of visits, this is a useful family to demonstrate that effect. Metrics which " \
            f"require coverage outside the WFD but are still sensitive to number of visits will show more " \
            f"complicated behavior as coverage in the NES and GP is reduced or increased. When the DDF " \
            f"fields are present, they are allocated 5% of the available survey time."  \
            f"<br>\n " \
            f"From these simulations we determined that between 1.65 and 1.7M visits  are required to " \
            f"cover 18K square degrees of the standard WFD to a minimum number of visits of 825 per " \
            f"pointing; some of the range in that required number of visits comes from over and under " \
            f"subscription in some parts of the sky, which leads to unevenness in coverage. "
        self.comment[key] = c
        self.family[key] = ['baseline_v1.5_10yrs',
                            'wfd_depth_scale0.65_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.70_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.75_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.80_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.85_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.90_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.95_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.99_noddf_v1.5_10yrs',
                            'wfd_depth_scale0.65_v1.5_10yrs',
                            'wfd_depth_scale0.70_v1.5_10yrs',
                            'wfd_depth_scale0.75_v1.5_10yrs',
                            'wfd_depth_scale0.80_v1.5_10yrs',
                            'wfd_depth_scale0.85_v1.5_10yrs',
                            'wfd_depth_scale0.90_v1.5_10yrs',
                            'wfd_depth_scale0.95_v1.5_10yrs',
                            'wfd_depth_scale0.99_v1.5_10yrs'
                            ]
        self.nicknames[key] = ['Baseline', '65% no DDF', '70% no DDF', '75% noDDF', '80% no DDF',
                               '85% no DDF', '90% no DDF', '95% noDDF', '99% no DDF',
                               '65%', '70%', '75%', '80%', '85%', '90%', '95%', '99%']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## filter_dist
        key = 'filter_dist'
        c = f"**{key}** = evaluate the impact of changing the balance of visits between filters. " \
            "Note that this family uses a simplified footprint that is a simple stripe of Declination " \
            "corresponding to the traditional WFD declination limits but no NES or SCP and continuing " \
            "WFD over the GP. Generally we find transients and variable stars metrics favor bluer " \
            "distributions of filters while solar system and galaxy metrics prefer redder " \
            "distributions of filters (particularly *i* band). <br> " \
            " ** the comparison run for this family is NOT the baseline, but rather one of the filter_dist " \
            "family, to avoid differences due to the footprint change. "
        self.comment[key] = c
        self.family[key] = ['filterdist_indx1_v1.5_10yrs',
                            'filterdist_indx2_v1.5_10yrs',
                            'filterdist_indx4_v1.5_10yrs',
                            'filterdist_indx3_v1.5_10yrs',
                            'filterdist_indx6_v1.5_10yrs',
                            'filterdist_indx5_v1.5_10yrs',
                            'filterdist_indx7_v1.5_10yrs',
                            'filterdist_indx8_v1.5_10yrs', ]
        self.nicknames[key] = ['Uniform',
                               'Baseline-like',
                               'u heavy',
                               'g heavy',
                               'i heavy',
                               'z and y heavy',
                               'Bluer',
                               'Redder']
        self.family_baseline[key] = 'filterdist_indx2_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ### footprint (stage 1)
        key = 'footprint'
        c = f"**{key}** = an initial large set of simulations exploring widely different options for the " \
            "overall survey footprint. The fraction of time devoted to the WFD will necessarily vary " \
            "among these simulations; this is one of the parameters suitable for later fine-tuning. " \
            "All runs in this family use 1x30s visits. Some of these footprints contain a traditional " \
            "WFD footprint, while others contain a shifted/extended N/S footprint that sometimes includes " \
            "a dust extinction limit around the galactic plane and sometimes a simple galactic latitude " \
            "cutoff; the bulges family is included because without significant galactic bulge coverage " \
            "metrics related to MW populations fell significantly, yet the time requirement to cover all " \
            "of the relevant areas together must be considered."
        self.comment[key] = c
        self.family[key] = ['filterdist_indx2_v1.5_10yrs',
                            'baseline_v1.5_10yrs',
                            'footprint_standard_goalsv1.5_10yrs',
                            'footprint_bluer_footprintv1.5_10yrs',
                            'footprint_no_gp_northv1.5_10yrs',
                            'footprint_gp_smoothv1.5_10yrs',
                            'footprint_add_mag_cloudsv1.5_10yrs',
                            'footprint_big_sky_dustv1.5_10yrs',
                            'footprint_big_skyv1.5_10yrs',
                            'footprint_big_sky_nouiyv1.5_10yrs',
                            'footprint_big_wfdv1.5_10yrs',
                            'footprint_newAv1.5_10yrs',
                            'footprint_newBv1.5_10yrs',
                            'bulges_bs_v1.5_10yrs',
                            'bulges_cadence_bs_v1.5_10yrs',
                            'bulges_bulge_wfd_v1.5_10yrs',
                            'bulges_cadence_bulge_wfd_v1.5_10yrs',
                            'bulges_i_heavy_v1.5_10yrs',
                            'bulges_cadence_i_heavy_v1.5_10yrs',
                            ]
        self.nicknames[key] = ['no nes',
                               'standard baseline',
                               'standard baseline again',
                               'bluer filters',
                               'no GP N extension',
                               'GP at WFD level',
                               'add MagClouds',
                               'big sky, dust-no GP',
                               'big sky - no GP',
                               'big sky - no GP, no uiy',
                               'big WFD',
                               'big sky + GP1 + NES',
                               'big sky + GP2 + NES',
                               'big sky + GP bulge',
                               'big sky + GP bulge cadenced',
                               'big sky + GP bulge @ WFD',
                               'big sky + GP bulge @WFD cadenced',
                               'big sky + GP i heavy',
                               'big sky + GP i heavy cadenced']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## footprint_tune
        key = 'footprint_tune'
        c = f"**{key}** = a further exploration of the survey footprint, exploring options " \
            "for improving the basic setup used in v1.6 in the 'combo_dust' simulation. " \
            "We feel combo_dust had a lot of promise, as it improved metrics for a wide range " \
            "of science without impacting metrics (currently avaialable in MAF) dramatically. " \
            "However, combo_dust had some issues, especially in terms of contingency available in " \
            "the WFD area (in case of exceptionally bad weather, it could fail SRD, and " \
            "as it was only one run, it did not offer variations to attempt to improve MWLV or TVS " \
            "science, for example). This footprint_tune family offers additional variations on " \
            "the combo_dust (shifted WFD with dust-extinction-limits) simulation. Generally the WFD here " \
            "is a dust-extinction limited footprint, but with variable N/S limits. We vary the coverage on " \
            "the remaining sky. " \
            "Because this is a v1.7 run, it cannot be compared directly with the footprint family above. " \
            "(they use 2x15s visits, not 1x30s). "
        self.comment[key] = c
        self.family[key] = ['baseline_nexp2_v1.7_10yrs',
                            'footprint_0_v1.710yrs',
                            'footprint_1_v1.710yrs',
                            'footprint_2_v1.710yrs',
                            'footprint_3_v1.710yrs',
                            'footprint_4_v1.710yrs',
                            'footprint_5_v1.710yrs',
                            'footprint_6_v1.710yrs',
                            'footprint_7_v1.710yrs',
                            'footprint_8_v1.710yrs']
        self.nicknames[key] = ['Traditional footprint',
                               'WFD -70.2<dec<7.8 + north ring',  # 0
                               'WFD -70.2<dec<7.8',  # 1
                               'WFD -67.4<dec<8',  # 2
                               'WFD -67.4<dec8 + 20deg bridge',  # 3
                               'WFD -62.5<dec<3.6 +33deg bridge',  # 4
                               'WFD -67.4<dec<8 + 20deg bridge (like 3)',  # 5
                               'WFD -67.4<dec<8 + 20deg bridge (south)',  # 6
                               'WFD -70.2<dec<7.8 no ecliptic in galaxy',  # 7
                               'WFD -70.2<dec<7.8 no galactic',  # 8
                               ]
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ### filter_cadence
        key = 'filter_cadence'
        c = f"**{key}** = investigate the impact of reducing the gaps between g band visits over the month, " \
            f"(essentially down-weighting the lunar cycle by adding a requirement that fields receive " \
            f"visits in g band filter throughout each month). In order to avoid 'long gaps' in g band " \
            f"coverage, additional fill-in visits in g are requested in each night; there is a limit to " \
            f"the number of fill-in visits in each night allowed, and these fill-in visits can be " \
            f"requested as contiguous blobs or non-contiguous pointings. The goal is to improve transient " \
            f"discovery for longer timescale transients which require bluer filter coverage (like SN)."
        self.comment[key] = c
        self.family[key] = ['baseline_nexp2_v1.7_10yrs',
                            'cadence_drive_gl30v1.7_10yrs',
                            'cadence_drive_gl30_gcbv1.7_10yrs',
                            'cadence_drive_gl100v1.7_10yrs',
                            'cadence_drive_gl100_gcbv1.7_10yrs',
                            'cadence_drive_gl200v1.7_10yrs',
                            'cadence_drive_gl200_gcbv1.7_10yrs',
                            ]
        self.nicknames[key] = ['Baseline',
                               'Add g, limit 30/night, non-contiguous',
                               'Add g, limit 30/night, contiguous',
                               'Add g, limit 100/night, non-contiguous',
                               'Add g, limit 100/night, contiguous',
                               'Add g, limit 200/night, non-contiguous',
                               'Add g, limit 200/night, contiguous']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        key = 'alt_rolling'
        c = f"**{key}** = a family of simulations that add alt-sched like nightly variations between " \
            f"the northern and southern portions of the sky. For some members of the family, a 2-band " \
            f"rolling cadence is also included (if 'roll' in the simulation name). Note that ALL of " \
            f"these footprints are a shifted WFD - extended N/S and using dust extinction to delineate " \
            f"the galactic plane. Few visits are placed into the GP or the NES or SCP. <br>" \
            f"The baseline for this run is tricky to pick; the standard baseline is a very different " \
            f"footprint, yet all runs in this family either add rolling OR add the alt-sched N/S " \
            f"modulation. For purposes of identifying the effects of the alt-sched algorithm, the run " \
            f"without alt-sched is chosen as the baseline.<br>"
        self.comment[key] = c
        self.family[key] = ['alt_dust_v1.5_10yrs',
                                    'alt_roll_mod2_dust_sdf_0.20_v1.5_10yrs',
                                    'roll_mod2_dust_sdf_0.20_v1.5_10yrs']
        self.nicknames[key] = ['Alt-sched modulation, no rolling',
                               'Alt-sched modulation, plus rolling',
                               'Standard sched, plus rolling']
        self.family_baseline[key] = 'roll_mod2_dust_sdf_0.20_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## rolling
        key = 'rolling'
        c = f"**{key}** = Add a rolling cadence, where some parts of the sky receive a higher number " \
            f"of visits during an 'on' season, followed by a lower number of visits during an 'off' " \
            f"season. During the first year and half, and the last year and half (or so), the sky is " \
            f"covered uniformly as normal. This 'intro' and 'outro' allows for better proper motion " \
            f"coverage, and is 1.5 years instead of 1 to allow the entire sky to receive even coverage " \
            f"during that period. This leaves 6 years for 'rolling'; simulations either split the sky " \
            f"into 2 or 3 declination-based regions which are covered either every other season or " \
            f"every third season. Each of the active regions is actually composed of 2 sub-section in " \
            f"the North and South, to spread follow-up requirements over the sky. Some simulations add " \
            f"an every-other nightly modulation between this northern and southern sub-section; some " \
            f"do not although this may happen to some extent due to 'blob' coverage."
        self.comment[key] = c
        self.family[key] = ['baseline_nexp2_v1.7_10yrs',
                            'rolling_nm_scale0.2_nslice2_v1.7_10yrs',
                            'rolling_nm_scale0.4_nslice2_v1.7_10yrs',
                            'rolling_nm_scale0.6_nslice2_v1.7_10yrs',
                            'rolling_nm_scale0.8_nslice2_v1.7_10yrs',
                            'rolling_nm_scale0.9_nslice2_v1.7_10yrs',
                            'rolling_nm_scale1.0_nslice2_v1.7_10yrs',
                            'rolling_nm_scale0.2_nslice3_v1.7_10yrs',
                            'rolling_nm_scale0.4_nslice3_v1.7_10yrs',
                            'rolling_nm_scale0.6_nslice3_v1.7_10yrs',
                            'rolling_nm_scale0.8_nslice3_v1.7_10yrs',
                            'rolling_nm_scale0.9_nslice3_v1.7_10yrs',
                            'rolling_nm_scale1.0_nslice3_v1.7_10yrs',
                            'rolling_scale0.2_nslice2_v1.7_10yrs',
                            'rolling_scale0.4_nslice2_v1.7_10yrs',
                            'rolling_scale0.6_nslice2_v1.7_10yrs',
                            'rolling_scale0.8_nslice2_v1.7_10yrs',
                            'rolling_scale0.9_nslice2_v1.7_10yrs',
                            'rolling_scale1.0_nslice2_v1.7_10yrs',
                            'rolling_scale0.2_nslice3_v1.7_10yrs',
                            'rolling_scale0.4_nslice3_v1.7_10yrs',
                            'rolling_scale0.6_nslice3_v1.7_10yrs',
                            'rolling_scale0.8_nslice3_v1.7_10yrs',
                            'rolling_scale0.9_nslice3_v1.7_10yrs',
                            'rolling_scale1.0_nslice3_v1.7_10yrs']
        self.nicknames[key] = ['Baseline',
                               'No Modulation, 0.2 strength, 2 band',
                               'No Modulation, 0.4 strength, 2 band',
                               'No Modulation, 0.6 strength, 2 band',
                               'No Modulation, 0.8 strength, 2 band',
                               'No Modulation, 0.9 strength, 2 band',
                               'No Modulation, 1.0 strength, 2 band',
                               'No Modulation, 0.2 strength, 3 band',
                               'No Modulation, 0.4 strength, 3 band',
                               'No Modulation, 0.6 strength, 3 band',
                               'No Modulation, 0.8 strength, 3 band',
                               'No Modulation, 0.9 strength, 3 band',
                               'No Modulation, 1.0 strength, 3 band',
                               '0.2 strength, 2 band',
                               '0.4 strength, 2 band',
                               '0.6 strength, 2 band',
                               '0.8 strength, 2 band',
                               '0.9 strength, 2 band',
                               '1.0 strength, 2 band',
                               '0.2 strength, 3 band',
                               '0.4 strength, 3 band',
                               '0.6 strength, 3 band',
                               '0.8 strength, 3 band',
                               '0.9 strength, 3 band',
                               '1.0 strength, 3 band']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        # MINISURVEYS

        ## twilight_neo
        key = 'twilight_neo'
        c = f"**{key}** = explore the impact of adding a twilight NEO survey, operating on various " \
            f"timescales and thus requiring varying fraction of survey time. These twilight NEO surveys " \
            f"replace the set initially released in  v1.5, improving the twilight NEO mini-survey " \
            f"performance for NEOs by restricting visits to low solar " \
            f"elongations. Twilight NEO visits are 1 second long, in r,i, and z filters."
        self.comment[key] = c
        self.family[key] = ['twi_neo_pattern1_v1.7_10yrs',
                            'twi_neo_pattern2_v1.7_10yrs',
                            'twi_neo_pattern3_v1.7_10yrs',
                            'twi_neo_pattern4_v1.7_10yrs',
                            'twi_neo_pattern5_v1.7_10yrs',
                            'twi_neo_pattern6_v1.7_10yrs',
                            'twi_neo_pattern7_v1.7_10yrs',
                            'baseline_nexp2_v1.7_10yrs']
        self.nicknames[key] = ['On every night',
                               'On every other night',
                               'On every third night',
                               'On every fourth night',
                               'On for 4 nights, off for 4 nights',
                               'On for 3 nights, off for 4 nights',
                               'On for 2 nights, off for 4 nights',
                               'Baseline (none)']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ## shortexp
        key = 'shortexp'
        c = f"**{key}** = explore the impact of adding 2 or 5 short exposures of 1 or 5 seconds each year " \
            f"(in all 6 filters). The number of visits in the entire survey increases -- but some will " \
            f"be too short to be useful for some science -- the amount of time used for the mini-survey " \
            f"varies in each of these examples, from 0.5% to 5%."
        self.comment[key] = c
        self.family[key] = ['short_exp_2ns_1expt_v1.5_10yrs',
                            'short_exp_2ns_5expt_v1.5_10yrs',
                            'short_exp_5ns_1expt_v1.5_10yrs',
                            'short_exp_5ns_5expt_v1.5_10yrs',
                            'baseline_v1.5_10yrs']
        self.nicknames[key] = ['2/yr x 1s',
                               '2/yr x 5s',
                               '5/yr x 1s',
                               '5/yr x 5s',
                               'Baseline (none)']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## dcr
        key = 'dcr'
        c = f"**{key}** = explore the impact of adding 1 or 2 high-airmass visits in various bandpasses " \
            f"each year, for the purpose of better-measuring differential chromatic refraction (helping " \
            f"with AGN redshifts and the creation of difference image templates). "
        self.comment[key] = c
        self.family[key] = ['dcr_nham1_ug_v1.5_10yrs',
                            'dcr_nham1_ugr_v1.5_10yrs',
                            'dcr_nham1_ugri_v1.5_10yrs',
                            'dcr_nham2_ug_v1.5_10yrs',
                            'dcr_nham2_ugr_v1.5_10yrs',
                            'dcr_nham2_ugri_v1.5_10yrs',
                            'baseline_v1.5_10yrs']
        self.nicknames[key] = ['1/yr in ug',
                               '1/yr in ugr',
                               '1/yr in ugri',
                               '2/yr in ug',
                               '2/yr in ugr',
                               '2/yr in ugri',
                               'Baseline (none)']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## good_seeing
        key = 'good_seeing'
        c = f"**{key}** = explore the effect of prioritizing achieving at least 1 'good seeing' image " \
            f"in the specified bandpasses in each year. These simulations do improve the seeing " \
            f"distributions in the targeted bands, compared to baseline -- this improvement is most " \
            f"visible when comparing the achieved IQ against the standard baseline, within a given year. "
        self.comment[key] = c
        self.family[key] = ['goodseeing_i_v1.5_10yrs',
                            'goodseeing_gi_v1.5_10yrs',
                            'goodseeing_gz_v1.5_10yrs',
                            'goodseeing_gri_v1.5_10yrs',
                            'goodseeing_griz_v1.5_10yrs',
                            'baseline_v1.5_10yrs', ]
        self.nicknames[key] = ['good i band',
                               'good gi bands',
                               'good gz bands',
                               'good gri bands',
                               'good griz bands',
                               'baseline - none']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ## spiders
        key = 'spiders'
        c = f"**{key}** = This example simulation explores rotating the camera so that diffraction " \
            f"spikes are aligned with the X/Y directions of the CCD, to reduce artifacts in " \
            f"difference imaging."
        self.comment[key] = c
        self.family[key] = ['spiders_v1.5_10yrs', 'baseline_v1.5_10yrs']
        self.nicknames[key] = ['Spiders Aligned', 'Random orientation']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ### DDF families
        # ddf sequences
        key = 'ddf'
        c = f"**{key}** = Vary the sequences for DDF fields. The amount of time per DDF field varies " \
            f"between some of these simulations."
        self.comment[key] = c
        self.family[key] = ['agnddf_v1.5_10yrs',
                            'descddf_v1.5_10yrs',
                            'daily_ddf_v1.5_10yrs',
                            'baseline_v1.5_10yrs']
        self.nicknames[key] = ['AGN sequences',
                               'DESC sequences',
                               'Daily sequences',
                               'Baseline']
        self.family_baseline[key] = 'baseline_v1.5_10yrs'
        self.family_version[key] = '1.5'

        ### DDF dithers
        key = 'ddf_dithers'
        c = f"**{key}** = Vary the translational dither offsets in the DDFs, from 0 to 2.0 degrees. " \
            f"Smaller dithers will help the overall depth and uniformity, but larger dithers may be " \
            f"needed for calibration."
        self.comment[key] = c
        self.family[key] = ['ddf_dither0.00_v1.7_10yrs',
                            'ddf_dither0.05_v1.7_10yrs',
                            'ddf_dither0.10_v1.7_10yrs',
                            'ddf_dither0.30_v1.7_10yrs',
                            'ddf_dither0.70_v1.7_10yrs',
                            'ddf_dither1.00_v1.7_10yrs',
                            'ddf_dither1.50_v1.7_10yrs',
                            'ddf_dither2.00_v1.7_10yrs',
                            'baseline_nexp2_v1.7_10yrs']
        self.nicknames[key] = ['0 dither',
                               '0.05 deg dither',
                               '0.10 deg dither',
                               '0.30 deg dither',
                               '0.70 deg dither',
                               '1.00 deg dither',
                               '1.50 deg dither',
                               '2.00 deg dither',
                               'Baseline (0.70 deg)']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        key = 'euclid_dithers'
        c = f"**{key}** = vary the translational dither offsets to fill in the Euclid DDF footprint, as the " \
            f"Euclid field is a double pointing for Rubin. These simulation vary the spatial dither both " \
            f"towards the second pointing and perpendicular to the second pointing. The perpendicular " \
            f"dithering is relatively small (and symmetric 'up' and 'down'). The dithering along the " \
            f"footprint ('direct') is larger and non-symmetric, with a smaller dither 'away' from the " \
            f"second pointing and a larger dither 'toward' the second pointing. (offsets are in degrees)."
        self.comment[key] = c
        self.family[key] = ['euclid_dither1_v1.7_10yrs',
                            'euclid_dither2_v1.7_10yrs',
                            'euclid_dither3_v1.7_10yrs',
                            'euclid_dither4_v1.7_10yrs',
                            'euclid_dither5_v1.7_10yrs',
                            'baseline_nexp2_v1.7_10yrs']
        self.nicknames[key] = ['Direct -0.25/+1.0, Perp +/-0.25 (deg)',
                               'Direct -0.1/+1.0, Perp +/-0.25 (deg)',
                               'Direct -0.25/+1.0, Perp +/-0.10 (deg)',
                               'Direct -0.25/+1.5, Perp +/-0.25 (deg)',
                               'Direct -0.25/+0.75, Perp +/-0.25 (deg',
                               'Baseline (random)']
        self.family_baseline[key] = 'baseline_nexp2_v1.7_10yrs'
        self.family_version[key] = '1.7'

        ## V1.6 potential schedulers (v16)
        key = 'potential_schedulers'
        c = f"**{key}** = A series of simulations where we vary *multiple* survey strategies at once, " \
            "trying to combine the survey strategies that seemed useful to us (at the time anyway) to " \
            "reach a particular science goal. These simulations are like cross-sections of the families, " \
            "using bits and pieces to try to reach goals, rather than explore the impact of the various " \
            "survey strategy changes individually. Each simulation is repeated for 2x15s visits and " \
            "for 1x30s visits. " \
            "<br>\n" \
            "The point here is to illustrate the effect of combinations of survey strategy variations; " \
            "some are successful and sometimes we may meet technical goals but not science goals. For " \
            "further details on each simulation, Section 5 in the cadence report for the " \
            "SCOC (https://pstn-051.lsst.io/) is recommended. "
        self.comment[key] = c
        self.family[key] = ['barebones_nexp2_v1.6_10yrs',
                            'barebones_v1.6_10yrs',
                            'baseline_nexp2_scaleddown_v1.6_10yrs',
                            'baseline_nexp2_v1.6_10yrs',
                            'baseline_nexp1_v1.6_10yrs',
                            'combo_dust_nexp2_v1.6_10yrs',
                            'combo_dust_v1.6_10yrs',
                            'ddf_heavy_nexp2_v1.6_10yrs',
                            'ddf_heavy_v1.6_10yrs',
                            'dm_heavy_nexp2_v1.6_10yrs',
                            'dm_heavy_v1.6_10yrs',
                            'mw_heavy_nexp2_v1.6_10yrs',
                            'mw_heavy_v1.6_10yrs',
                            'rolling_exgal_mod2_dust_sdf_0.80_nexp2_v1.6_10yrs',
                            'rolling_exgal_mod2_dust_sdf_0.80_v1.6_10yrs',
                            'ss_heavy_nexp2_v1.6_10yrs',
                            'ss_heavy_v1.6_10yrs']
        self.nicknames[key] = ['WFD only 2x15s', 'WFD only 1x30s',
                               'Baseline 2x15s adjusted WFD fraction', 'Baseline 2x15s', 'Baseline 1x30s',
                               'Combo dust 2x15s', 'Combo dust 1x30s',
                               'DDF 13.4 % 2x15s', 'DDF 13.4% 1x30s',
                               'DM heavy 2x15s', 'DM heavy 1x30s',
                               'Bulge/MC @ WFD 2x15s', 'Bulge/MC @ WFD 1x30s',
                               'Shifted rolling WFD 2x15s', 'Shifted rolling WFD 1x30s',
                               'Twilight pairs + NEO 2x15s', 'Twilight pairs + NEO 1x30s']
        self.family_baseline[key] = 'baseline_nexp1_v1.6_10yrs'
        self.family_version[key] = '1.6'

        """
        ## filtercadence
        key = 'even_filters'
        c = f"**{key}** = choose to observe in bluer bandpasses even when the moon is full. This was the first " \
            f"round of simulations to investigate this effect - see also the 'cadence_drive' family. "
        self.family[key] = ['even_filters_alt_g_v1.6_10yrs',
                                  'even_filters_altv1.6_10yrs',
                                  'even_filters_g_v1.6_10yrs',
                                  'even_filtersv1.6_10yrs',
                                  'baseline_nexp1_v1.6_10yrs'
                                  ]
        self.nicknames[key] = self.family[key]
        self.family_baseline[key] = 'baseline_nexp1_v1.6_10yrs'
        self.family_version[key] = '1.5'
        
        self.comment['greedy'] = 'greedy = look at the impact of changing the `greedy` visits during 
                                twilight to exclude the ecliptic. This should push all ecliptic visits 
                                into pairs. This did not make a significant difference, and now we have 
                                simulations that actually program pairs during twilight. '
        self.family['greedy'] = ['greedy_footprint_v1.5_10yrs',
                            'baseline_v1.5_10yrs']
        self.nicknames['greedy'] = ['greedy', 'baseline']
        self.family_baseline['greedy'] = 'baseline_v1.5_10yrs'
        self.family_version['greedy'] = '1.5'
        
        self.comment['u60'] = 'u60 = simulation extending u band visits to 60s but not doubling the number 
                                of visits. This was pretty disastrous for transients. Replaced by u_long.'
        self.family['u60'] = ['u60_v1.5_10yrs',
                         'baseline_v1.5_10yrs']
        self.nicknames['u60'] = ['u60 fewer visits', 'baseline']
        self.family_baseline['u60'] = 'baseline_v1.5_10yrs'
        self.family_version['u60'] = '1.5'        
        """

    def read_summary_csv(self, csv_file='all_summaries_2021_02_08.csv'):
        """Read the summary stat csv file from disk.
        This file can be downloaded from:
        https://epyc.astro.washington.edu/~lynnej/opsim_downloads/all_summaries_2021_02_08.csv
        """
        # Read in the CSV file containing the summary stat information (
        self.summaries = pd.read_csv(csv_file, index_col=0)

    def list_of_families(self):
        """Print a list of the simulation groups under consideration, as of this time. """
        # The families
        total = 0
        displaystring = ''
        family_list = []
        for k in self.family:
            if k == 'version_baselines':
                continue
            family_list.append(k)
            displaystring+= f"**{k}**, with {len(self.family[k])} simulations.<br>"
            total += len(self.family[k])
        display_markdown(displaystring, raw=True)
        print(f'For {total} simulations in all.')
        return family_list

    def family_info(self, f, normalized=False):
        """Print some summary information about the family and return a high-level set of metrics."""
        d = pd.DataFrame(self.summaries[tablemetrics].loc[self.family[f]])
        if normalized:
            d = d/self.summaries[tablemetrics].loc[self.family_baseline[f]]
        d.columns = tablenames
        d['Briefly'] = self.nicknames[f]
        display_markdown(self.comment[f], raw=True)
        print(f"Comparison run: {self.family_baseline[f]}")
        return d

    def plot_areaNvis(self, f):
        metrics = tablemetrics[0:4]
        names = tablenames[0:4]
        d = self.summaries[metrics].loc[self.family[f]]
        nd = norm_df(d, self.family_baseline[f])
        nd.columns = names
        plot(nd, normed=True, figsize=(10, 6), style=['k-', 'k:', 'r-', 'r:'])
        plt.xlim(0, len(nd)-1)
        xlims = plt.xlim()
        if plt.ylim()[0] < 0.50:
            plt.ylim(bottom=0.50)
        if plt.ylim()[1] > 1.5:
            plt.ylim(top=1.5)
        plt.fill_between(xlims, 1.05, plt.ylim()[1], color='g', alpha=0.1)
        plt.fill_between(xlims, 0.95, plt.ylim()[0], color='r', alpha=0.1)


## Some utility functions to normalize a dataframe or plot it - useful for summar stat comparisons

def norm_df(df, norm_run,
            invert_cols=None, reverse_cols=None, mag_cols=None):
    """
    Normalize values in a DataFrame, based on the values in a given run.
    Can normalize some columns (metric values) differently (invert_cols, reverse_cols, mag_cols)
    if those columns are specified; this lets the final normalized dataframe 'look' the same way
    in a plot (i.e. "up" is better (reverse_cols), they center on 1 (mag_cols), and the magnitude scales
    as expected (invert_cols)).

    Parameters
    ----------
    df : pd.DataFrame
        The data frame containing the metric values to compare
    norm_run: str
        The name of the simulation to normalize to (typically family_baseline)
    invert_cols: list
        Columns (metric values) to convert to 1 / value
    reverse_cols: list
        Columns (metric values) to invert (-1 * value)
    mag_cols: list
        Columns (metrics values) to treat as magnitudes (1 + (difference from norm_run))

    Returns
    -------
    pd.DataFrame
        Normalized data frame
    """
    # Copy the dataframe but drop the columns containing only strings
    out_df = df.copy()
    if reverse_cols is not None:
        out_df[reverse_cols] = -out_df[reverse_cols]
    if invert_cols is not None:
        out_df[invert_cols] = 1 / out_df[invert_cols]
    if mag_cols is not None:
        out_df[mag_cols] = 1 + out_df[mag_cols] - out_df[mag_cols].loc[norm_run]
    else:
        mag_cols = []
    # which columns are strings?
    string_cols = [c for c, t in zip(df.columns, df.dtypes) if t == 'object']
    cols = [c for c in out_df.columns.values if not (c in mag_cols or c in string_cols)]
    out_df[cols] = 1 + (out_df[cols] - out_df[cols].loc[norm_run]) / out_df[cols].loc[norm_run]
    return out_df

def plot(df, normed=True, style=None, figsize=(10, 6), run_nicknames=None):
    """Plot a DataFrame of metric values.

    Parameters
    ---------
    df: pd.DataFrame
        The dataframe of metric values to plot
    normed: bool, opt
        Is the dataframe normalized or not? (default True)
        If true, adds +/- 5% lines to output
    style: list, opt
        Optional list of line color/style values to use for the plotted metric values
    figsize: tuple, opt
        Figure size
    run_nicknames: list, opt
        Replace the run names in the dataframe with these nicknames
    """
    df.plot(figsize=figsize, style=style)
    plt.legend(loc=(1.01, 0))
    if normed:
        plt.axhline(0.95, alpha=0.3, linestyle=':')
        plt.axhline(1.0, alpha=0.3, linestyle='--')
        plt.axhline(1.05, alpha=0.3, linestyle=':')
    if run_nicknames is not None:
        xnames = run_nicknames
    else:
        xnames = df.index.values
    xi = np.arange(len(xnames))
    plt.xticks(xi, xnames, rotation=90, fontsize='large')
    plt.xlim(0, len(xnames)-1)
    plt.grid('k:', alpha=0.3)
    plt.tight_layout()


def fO_cutoff(df, norm_run):
    """Calculate the Y value for a cutoff line where the fO metric fails SRD req.
    This location changes according to the scaling from the baseline for the family.
    """
    srd_fO_cutoff = df['fONv MedianNvis fO All visits HealpixSlicer'].loc[norm_run]
    srd_fO_cutoff = 825 / srd_fO_cutoff
    return srd_fO_cutoff


def special_family_plots(f, families):
    if f == 'footprint':
        # for footprints, let's add shading for similar kinds of footprints
        ylims = plt.ylim()
        plt.fill_between([0, 0.5], ylims[0], ylims[1], alpha=0.1, color='olive')
        plt.fill_between([0.5, 6.5], ylims[0], ylims[1], alpha=0.1, color='mistyrose')
        plt.fill_between([6.5, 9.5], ylims[0], ylims[1], alpha=0.1, color='yellowgreen')
        plt.fill_between([9.5, 18], ylims[0], ylims[1], alpha=0.1, color='darkorange')
    if f == 'rolling':
        ylims = plt.ylim()
        plt.fill_between([0, 0.5], ylims[0], ylims[1], alpha=0.1, color='olive')
        plt.fill_between([0.5, 6.5], ylims[0], ylims[1], alpha=0.1, color='mistyrose')
        plt.fill_between([6.5, 12.5], ylims[0], ylims[1], alpha=0.1, color='darkorange')
        plt.fill_between([12.5, 18.5], ylims[0], ylims[1], alpha=0.1, color='lightgreen')
        plt.fill_between([18.5, 25], ylims[0], ylims[1], alpha=0.1, color='darkgreen')
    if f == 'potential schedulers':
        ylims = plt.ylim()
        # shade the nexp2 runs
        xnames = families.family[f]
        nexp2 = np.zeros(len(xnames))
        for i, x in enumerate(xnames):
            if 'nexp2' in x:
                nexp2[i] = 1
        shadesx1 = np.where(nexp2 == 1)[0] - 0.5
        shadesx2 = np.where(nexp2 == 1)[0] + 0.5
        for x1, x2 in zip(shadesx1, shadesx2):
            plt.fill_between([x1, x2], ylims[0], ylims[1], alpha=0.1, color='olive')
    return