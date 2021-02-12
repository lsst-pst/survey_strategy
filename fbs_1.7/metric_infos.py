## Dictionaries containing sets of metrics which have been plotted in PTSN-051 or found otherwise useful

metrics = {}
short_names = {}
short_names_norm = {}
invert_cols = {}
mag_cols = {}
styles = {}

radarmetrics = ['fONv MedianNvis fO All visits HealpixSlicer',
                'Mean WeakLensingNvisits fiveSigmaDepth, visitExposureTime i band non-DD HealpixSlicer',
                '3x2ptFoM ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                'SNIa_PrePeak non-DD UserPointsSlicer',
                'TDEsPopMetric__some_color_pu  UserPointsSlicer',
                'Fast Microlensing  UserPointsSlicer',
                'Median Parallax Error (18k) Parallax Error @ 22.4 All visits HealpixSlicer',
                'Median Proper Motion Error (18k) Proper Motion Error @ 20.5 All visits HealpixSlicer',
                'N stars to Precision 0.20  r HealpixSlicer',
                'N Galaxies (all) GalaxyCountsMetric_extended i band HealpixSlicer',
                '3 pairs in 15 nights detection loss NEO H=16.0',
                '3 pairs in 15 nights detection loss NEO H=22.0',
                '3 pairs in 15 nights detection loss TNO H=6.0',
                ]
radarnames = ['fONv_med',
              'WL',
              '3x2pt FoM',
              'SNIa',
              'TDE',
              'Fast Microlensing',
              'Parallax',
              'Proper motion',
              'N Stars',
              ' N Galaxies',
              '   NEO, big',
              '   NEO, small',
              'TNO, big']
invertradar = ['Median Parallax Error (18k) Parallax Error @ 22.4 All visits HealpixSlicer',
               'Median Proper Motion Error (18k) Proper Motion Error @ 20.5 All visits HealpixSlicer', ]

metrics['srd'] = ['fONv MedianNvis fO All visits HealpixSlicer',
                  'Median Parallax Error (18k) Parallax Error @ 22.4 All visits HealpixSlicer',
                  'Median Parallax Error (18k) Parallax Error @ 24.0 All visits HealpixSlicer',
                  'Median Proper Motion Error (18k) Proper Motion Error @ 20.5 All visits HealpixSlicer',
                  'Median Proper Motion Error (18k) Proper Motion Error @ 24.0 All visits HealpixSlicer',
                  ]
short_names['srd'] = ['fONv MedianNvis',
                      'Med Parallax Error @22.4',
                      'Med Parallax Error @24.0',
                      'Med PM Error @20.5',
                      'Med PM Error @24.0']
short_names_norm['srd'] = ['fONv MedianNvis',
                           '1 / Med Parallax Error @22.4',
                           '1 / Med Parallax Error @24.0',
                           '1 / Med PM Error @20.5',
                           '1 /Med PM Error @24.0']
invert_cols['srd'] = ['Median Parallax Error (18k) Parallax Error @ 22.4 All visits HealpixSlicer',
                      'Median Parallax Error (18k) Parallax Error @ 24.0 All visits HealpixSlicer',
                      'Median Proper Motion Error (18k) Proper Motion Error @ 20.5 All visits HealpixSlicer',
                      'Median Proper Motion Error (18k) Proper Motion Error @ 24.0 All visits HealpixSlicer', ]
styles['srd'] = ['k-', 'c-', 'c:', 'r-', 'r:']

metrics['Nvis'] = ['Nvisits All',
                   'Nvisits Long Exp',
                   'Nvisits Long WFD',
                   'OpenShutterFraction All visits',
                   'Mean NVisits u band HealpixSlicer',
                   'Mean NVisits g band HealpixSlicer',
                   'Mean NVisits r band HealpixSlicer',
                   'Mean NVisits i band HealpixSlicer',
                   'Mean NVisits z band HealpixSlicer',
                   'Mean NVisits y band HealpixSlicer',
                   ]
short_names['Nvis'] = ['Nvisits (all)', 'Nvisits (long exp)', 'Nvisits (long exp WFD)',
                       'OpenShutterFraction',
                       'Mean Nvisits u', 'Mean Nvisits g', 'Mean Nvisits r',
                       'Mean Nvisits i', 'Mean Nvisits z', 'Mean Nvisits y', ]
mag_cols['Nvis'] = None
styles['Nvis'] = ['b-.', 'b-', 'r-.', 'g--', 'c:', 'g:', 'y:', 'r:', 'm:', 'k:']

metrics['cadence'] = [
    'Median Median Intra-Night Gap  HealpixSlicer',
    'Mean Median Inter-Night Gap u band HealpixSlicer',
    'Mean Median Inter-Night Gap r band HealpixSlicer',
    'Mean Median Inter-Night Gap y band HealpixSlicer',
    #  'Mean Median Season Length all bands HealpixSlicer', Seasonlength has issues in 1.5
]
short_names['cadence'] = ['Intra-Night Gap',
                          'Inter-Night Gap u',
                          'Inter-Night Gap r',
                          'Inter-Night Gap y',
                          #    'Season Length',
                          ]
short_names_norm['cadence'] = ['1 / Intra-Night Gap',
                               '1 / Inter-Night Gap u',
                               '1 / Inter-Night Gap r',
                               '1 / Inter-Night Gap y',
                               # '1 / Season Length',
                               ]
invert_cols['cadence'] = ['Median Median Intra-Night Gap  HealpixSlicer',
                          'Mean Median Inter-Night Gap u band HealpixSlicer',
                          'Mean Median Inter-Night Gap r band HealpixSlicer',
                          'Mean Median Inter-Night Gap y band HealpixSlicer',
                          # 'Mean Median Season Length all bands HealpixSlicer',
                          ]
styles['cadence'] = ['b:', 'c--', 'r--', 'k--', ]  # 'g-.']

metrics['tvs'] = ['Mean PeriodDetection P_0.5_Mag_21_Amp_0.05-0.1-1 HealpixSlicer',
                  # 'Mean PeriodDetection P_1.0_Mag_21_Amp_0.05-0.1-1 HealpixSlicer',
                  # 'Mean PeriodDetection P_2.0_Mag_21_Amp_0.05-0.1-1 HealpixSlicer',
                  'Fast Microlensing  UserPointsSlicer',
                  # 'Slow Microlensing  UserPointsSlicer',
                  # 'KN_Detected  UserPointsSlicer',
                  # 'KN_PrePeak  UserPointsSlicer',
                  # 'KN_WellSampled  UserPointsSlicer',
                  # 'TDEsPopMetric__prepeak  UserPointsSlicer',
                  # 'TDEsPopMetric__some_color  UserPointsSlicer',
                  'TDEsPopMetric__some_color_pu  UserPointsSlicer',
                  # 'SNIa_Detected non-DD UserPointsSlicer',
                  'SNIa_PrePeak non-DD UserPointsSlicer',
                  'SNIa_WellSampled non-DD UserPointsSlicer',
                  'N stars to Precision 0.20  r HealpixSlicer',
                  'N stars to Precision 0.20  y HealpixSlicer']
short_names['tvs'] = ['Mean PeriodDetection P=0.5 days',
                      # 'Mean PeriodDetection P=1.0 days',
                      # 'Mean PeriodDetection P=2.0 days',
                      'Fast microlensing',
                      # 'Slow microlensing',
                      # 'KN Detected', 'KN PrePeak', 'KN WellSampled',
                      # 'TDE PrePeak', 'TDE AnyColor',
                      'TDE AnyColor + u',
                      # 'SNIa Detected',
                      'SNIa PrePeak', 'SNIa WellSampled',
                      'Nstars Precision<0.2mag r', 'Nstars Precision<0.2mag y']
styles['tvs'] = ['k-', 'c-', 'b:', 'g:', 'g--', 'm--', 'r--']

metrics['descWFD'] = ['Median ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                      'Rms ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                      'Effective Area (deg) ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                      '3x2ptFoM ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer',
                      'N Galaxies (all) DepthLimitedNumGalaxiesMetric i band galaxies non-DD HealpixSlicer',
                      'Mean WeakLensingNvisits fiveSigmaDepth, visitExposureTime i band non-DD HealpixSlicer',
                      ]
short_names['descWFD'] = ['Median coaddedM5 i band',
                          'RMS coaddedM5 i band',
                          'Effective survey area',
                          '3x2pt FoM',
                          'NGal in exgal footprint',
                          'Mean NVisits (WL)']
short_names_norm['descWFD'] = ['Median coaddedM5 i band',
                               '1 / RMS coaddedM5 i band',
                               'Effective survey area',
                               '3x2pt FoM',
                               'NGal in exgal footprint',
                               'Mean NVisits (WL)']
invert_cols['descWFD'] = ['Rms ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer']
mag_cols['descWFD'] = ['Median ExgalM5_with_cuts i band non-DD year 10 HealpixSlicer']
styles['descWFD'] = ['b-.', 'b:', 'b-', 'r-.', 'm:', 'g-']

metrics['galaxies'] = ['N Galaxies (all) GalaxyCountsMetric_extended i band HealpixSlicer']
short_names['galaxies'] = ['NGal all sky']

metrics['sso'] = ['3 pairs in 15 nights detection loss PHA H=16.0',
                  '3 pairs in 15 nights detection loss PHA H=22.0',
                  '3 pairs in 15 nights detection loss NEO H=16.0',
                  '3 pairs in 15 nights detection loss NEO H=22.0',
                  '3 pairs in 15 nights detection loss MBA H=16.0',
                  '3 pairs in 15 nights detection loss MBA H=21.0',
                  '3 pairs in 15 nights detection loss Trojan H=14.0',
                  '3 pairs in 15 nights detection loss Trojan H=18.0',
                  '3 pairs in 15 nights detection loss TNO H=6.0',
                  '3 pairs in 15 nights detection loss TNO H=8.0', ]
short_names['sso'] = ['Completeness PHA H<16.0',
                      'Completeness PHA H<22.0',
                      'Completeness NEO H<16.0',
                      'Completeness NEO H<22.0',
                      'Completeness MBA H<16.0',
                      'Completeness MBA H<21.0',
                      'Completeness Trojan H<14.0',
                      'Completeness Trojan H<18.0',
                      'Completeness TNO H<6.0',
                      'Completeness TNO H<8.0', ]
styles['sso'] = ['g-', 'g--', 'b-', 'b--', 'y-', 'y--', 'c-', 'c--', 'r-', 'r--']

sso_metrics = {}
sso_short_names = {}
sso_linestyles = ['g-', 'g--', 'b-', 'b--', 'y-', 'y--', 'c-', 'c--', 'r-', 'r--']

sso_metrics['sso disc'] = ['3 pairs in 15 nights detection loss PHA H=16.0',
                           '3 pairs in 15 nights detection loss PHA H=22.0',
                           '3 pairs in 15 nights detection loss NEO H=16.0',
                           '3 pairs in 15 nights detection loss NEO H=22.0',
                           '3 pairs in 15 nights detection loss MBA H=16.0',
                           '3 pairs in 15 nights detection loss MBA H=21.0',
                           '3 pairs in 15 nights detection loss Trojan H=14.0',
                           '3 pairs in 15 nights detection loss Trojan H=18.0',
                           '3 pairs in 15 nights detection loss TNO H=6.0',
                           '3 pairs in 15 nights detection loss TNO H=8.0', ]
sso_short_names['sso disc'] = ['Completeness PHA H<16.0',
                               'Completeness PHA H<22.0',
                               'Completeness NEO H<16.0',
                               'Completeness NEO H<22.0',
                               'Completeness MBA H<16.0',
                               'Completeness MBA H<21.0',
                               'Completeness Trojan H<14.0',
                               'Completeness Trojan H<18.0',
                               'Completeness TNO H<6.0',
                               'Completeness TNO H<8.0', ]

sso_metrics['Lightcurve Inversion'] = ['FractionPop Lightcurve Inversion PHA H=16.0',
                                       'FractionPop Lightcurve Inversion PHA H=19.0',
                                       'FractionPop Lightcurve Inversion NEO H=16.0',
                                       'FractionPop Lightcurve Inversion NEO H=19.0',
                                       'FractionPop Lightcurve Inversion MBA H=16.0',
                                       'FractionPop Lightcurve Inversion MBA H=18.0',
                                       'FractionPop Lightcurve Inversion Trojan H=14.0',
                                       'FractionPop Lightcurve Inversion Trojan H=15.0']
sso_short_names['Lightcurve Inversion'] = ['Fraction LC Inversion PHA H=16.0',
                                           'Fraction LC Inversion PHA H=19.0',
                                           'Fraction LC Inversion NEO H=16.0',
                                           'Fraction LC Inversion NEO H=19.0',
                                           'Fraction LC Inversion MBA H=16.0',
                                           'Fraction LC Inversion MBA H=18.0',
                                           'Fraction LC Inversion Trojan H=14.0',
                                           'Fraction LC Inversion Trojan H=15.0']

sso_metrics['Fraction Pop 3 bands'] = ['FractionPop 2 of g, r or i, z or y PHA H=16.0',
                                       'FractionPop 2 of g, r or i, z or y PHA H=19.0',
                                       'FractionPop 2 of g, r or i, z or y NEO H=16.0',
                                       'FractionPop 2 of g, r or i, z or y NEO H=19.0',
                                       'FractionPop 2 of g, r or i, z or y MBA H=16.0',
                                       'FractionPop 2 of g, r or i, z or y MBA H=18.0',
                                       'FractionPop 2 of g, r or i, z or y Trojan H=14.0',
                                       'FractionPop 2 of g, r or i, z or y Trojan H=15.0',
                                       'FractionPop 3 filters TNO H=6.0',
                                       'FractionPop 3 filters TNO H=7.0', ]
sso_short_names['Fraction Pop 3 bands'] = ['Fraction 3 of g and (r or i) and (z or y) PHA H=16.0',
                                           'Fraction 3 of g and (r or i) and (z or y) PHA H=19.0',
                                           'Fraction 3 of g and (r or i) and (z or y) NEO H=16.0',
                                           'Fraction 3 of g and (r or i) and (z or y) NEO H=19.0',
                                           'Fraction 3 of g and (r or i) and (z or y) MBA H=16.0',
                                           'Fraction 3 of g and (r or i) and (z or y) MBA H=18.0',
                                           'Fraction 3 of g and (r or i) and (z or y) Trojan H=14.0',
                                           'Fraction 3 of g and (r or i) and (z or y) Trojan H=15.0',
                                           'Fraction 3 filters TNO H=6.0',
                                           'Fraction 3 filters TNO H=7.0', ]

sso_metrics['Fraction Pop 4 bands'] = ['FractionPop 4 of grizy PHA H=16.0',
                                       'FractionPop 4 of grizy PHA H=19.0',
                                       'FractionPop 4 of grizy NEO H=16.0',
                                       'FractionPop 4 of grizy NEO H=19.0',
                                       'FractionPop 4 of grizy MBA H=16.0',
                                       'FractionPop 4 of grizy MBA H=18.0',
                                       'FractionPop 4 of grizy Trojan H=14.0',
                                       'FractionPop 4 of grizy Trojan H=15.0',
                                       'FractionPop 4 filters TNO H=6.0',
                                       'FractionPop 4 filters TNO H=7.0', ]
sso_short_names['Fraction Pop 4 bands'] = ['Fraction 4 of grizy PHA H=16.0',
                                           'Fraction 4 of grizy PHA H=19.0',
                                           'Fraction 4 of grizy NEO H=16.0',
                                           'Fraction 4 of grizy NEO H=19.0',
                                           'Fraction 4 of grizy MBA H=16.0',
                                           'Fraction 4 of grizy MBA H=18.0',
                                           'Fraction 4 of grizy Trojan H=14.0',
                                           'Fraction 4 of grizy Trojan H=15.0',
                                           'Fraction 4 filters TNO H=6.0',
                                           'Fraction 4 filters TNO H=7.0', ]

sso_metrics['Fraction Pop 5 bands'] = ['FractionPop 5 of grizy PHA H=16.0',
                                       'FractionPop 5 of grizy PHA H=19.0',
                                       'FractionPop 5 of grizy NEO H=16.0',
                                       'FractionPop 5 of grizy NEO H=19.0',
                                       'FractionPop 5 of grizy MBA H=16.0',
                                       'FractionPop 5 of grizy MBA H=18.0',
                                       'FractionPop 5 of grizy Trojan H=14.0',
                                       'FractionPop 5 of grizy Trojan H=15.0',
                                       'FractionPop 5 filters TNO H=6.0',
                                       'FractionPop 5 filters TNO H=7.0', ]
sso_short_names['Fraction Pop 5 bands'] = ['Fraction with grizy PHA H=16.0',
                                           'Fraction with grizy PHA H=19.0',
                                           'Fraction with grizy NEO H=16.0',
                                           'Fraction with grizy NEO H=19.0',
                                           'Fraction with grizy MBA H=16.0',
                                           'Fraction with grizy MBA H=18.0',
                                           'Fraction with grizy Trojan H=14.0',
                                           'Fraction with grizy Trojan H=15.0',
                                           'Fraction with 5 filters TNO H=6.0',
                                           'Fraction with 5 filters TNO H=7.0', ]

sso_metrics['Fraction Pop 6 bands'] = ['FractionPop 6 of ugrizy PHA H=16.0',
                                       'FractionPop 6 of ugrizy PHA H=19.0',
                                       'FractionPop 6 of ugrizy NEO H=16.0',
                                       'FractionPop 6 of ugrizy NEO H=19.0',
                                       'FractionPop 6 of ugrizy MBA H=16.0',
                                       'FractionPop 6 of ugrizy MBA H=18.0',
                                       'FractionPop 6 of ugrizy Trojan H=14.0',
                                       'FractionPop 6 of ugrizy Trojan H=15.0',
                                       'FractionPop 6 filters TNO H=6.0',
                                       'FractionPop 6 filters TNO H=7.0']
sso_short_names['Fraction Pop 6 bands'] = ['Fraction with ugrizy PHA H=16.0',
                                           'Fraction with ugrizy PHA H=19.0',
                                           'Fraction with ugrizy NEO H=16.0',
                                           'Fraction with ugrizy NEO H=19.0',
                                           'Fraction with ugrizy MBA H=16.0',
                                           'Fraction with ugrizy MBA H=18.0',
                                           'Fraction with ugrizy Trojan H=14.0',
                                           'Fraction with ugrizy Trojan H=15.0',
                                           'Fraction with 6 filters TNO H=6.0',
                                           'Fraction with 6 filters TNO H=7.0', ]

for m in metrics:
    if m not in invert_cols:
        invert_cols[m] = None
    if m not in mag_cols:
        mag_cols[m] = None
    if m not in styles:
        styles[m] = None
    if m not in short_names_norm:
        short_names_norm[m] = short_names[m]
