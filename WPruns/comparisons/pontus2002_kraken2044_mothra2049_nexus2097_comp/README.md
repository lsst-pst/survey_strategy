# Table of Contents
1. [fO](#fo)
2. [Total Effective Time](#total-effective-time)
3. [Normalized Effective Time](#normalized-effective-time)
4. [Open Shutter Fraction](#open-shutter-fraction)
5. [Parallax](#parallax)
6. [Proper Motion](#proper-motion)
7. [Rapid Revisit](#rapid-revisit)
8. [Fraction in Pairs](#fraction-in-paris)
9. [Slews](#slews)
10. [Filter Changes](#filter-changes)
11. [Nvisits](#nvisits)
12. [Proposal Fractions](#proposal-fractions)
13. [Median Nvisits WFD](#median-nvisits-wfd)
14. [Median CoaddM5 WFD](#median-coaddm5-wfd)
15. [Median FiveSigmaDepth](#median-fivesigmadepth)
16. [Median Internight Gap](#median-internight-gap)
17. [Median Airmass WFD](#median-airmass-wfd)
18. [Median Seeing WFD](#median-seeing-wfd)
19. [Skymap comparisons](#skymap-comparisons)
20. [Histogram comparisons](#histogram-comparisons)
# fO
|                                                       |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| fOArea fO All visits HealpixSlicer                    |      6061.38  |      6061.38  |      6061.38  |     6061.38  |
| fOArea/benchmark fO All visits HealpixSlicer          |         0.337 |         0.337 |         0.337 |        0.337 |
| fONv MedianNvis fO All visits HealpixSlicer           |       713     |       719     |       740     |      721     |
| fONv MinNvis fO All visits HealpixSlicer              |       682     |       688     |       694     |      692     |
| fONv/benchmark MedianNvis fO All visits HealpixSlicer |         0.864 |         0.872 |         0.897 |        0.874 |
| fONv/benchmark MinNvis fO All visits HealpixSlicer    |         0.827 |         0.834 |         0.841 |        0.839 |
| fOArea fO WFD HealpixSlicer                           |      6028.65  |      6028.65  |      6028.65  |     6028.65  |
| fOArea/benchmark fO WFD HealpixSlicer                 |         0.335 |         0.335 |         0.335 |        0.335 |
| fONv MedianNvis fO WFD HealpixSlicer                  |       713     |       719     |       740     |      721     |
| fONv MinNvis fO WFD HealpixSlicer                     |       682     |       688     |       694     |      692     |
| fONv/benchmark MedianNvis fO WFD HealpixSlicer        |         0.864 |         0.872 |         0.897 |        0.874 |
| fONv/benchmark MinNvis fO WFD HealpixSlicer           |         0.827 |         0.834 |         0.841 |        0.839 |

# Total Effective Time
|                          |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-------------------------|--------------:|--------------:|--------------:|-------------:|
| Total Teff all bands     |   3.99238e+07 |   3.99424e+07 |   3.80749e+07 |  3.89278e+07 |
| Total Teff WFD all bands |   3.81058e+07 |   3.81273e+07 |   3.6762e+07  |  3.75834e+07 |

# Normalized Effective Time
|                                                    |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:---------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Normalized Teff WFD all bands HealpixSlicer |         0.575 |         0.57  |         0.54  |        0.552 |
| Normalized Teff WFD all bands HealpixSlicer        |     31568     |     31568     |     31568     |    31568     |
| Normalized Teff WFD all bands                      |         0.547 |         0.543 |         0.518 |        0.531 |

# Open Shutter Fraction
|                                                 |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| OpenShutterFraction All visits                  |         0.733 |         0.74  |         0.74  |        0.738 |
| Median OpenShutterFraction Per night OneDSlicer |         0.736 |         0.743 |         0.747 |        0.742 |
| OpenShutterFraction Per night OneDSlicer        |      3025     |      3025     |      3025     |     3025     |

# Parallax
|                                                                |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:---------------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Parallax Error @ 22.4 All visits HealpixSlicer          |         1.955 |         1.964 |         2.056 |        2.019 |
| Median Parallax Error @ 24.0 All visits HealpixSlicer          |         7.613 |         7.696 |         8.083 |        7.934 |
| Median Parallax Coverage @ 22.4 All visits HealpixSlicer       |         0.559 |         0.583 |         0.559 |        0.574 |
| Median Parallax Coverage @ 24.0 All visits HealpixSlicer       |         0.555 |         0.579 |         0.555 |        0.57  |
| Median Parallax-DCR degeneracy @ 22.4 All visits HealpixSlicer |         0.194 |         0.252 |         0.242 |        0.308 |
| Median Parallax-DCR degeneracy @ 24.0 All visits HealpixSlicer |         0.19  |         0.252 |         0.235 |        0.306 |
| Median Parallax Error @ 22.4 WFD HealpixSlicer                 |         1.959 |         1.964 |         2.056 |        2.019 |
| Median Parallax Error @ 24.0 WFD HealpixSlicer                 |         7.623 |         7.7   |         8.087 |        7.937 |
| Median Parallax Coverage @ 22.4 WFD HealpixSlicer              |         0.559 |         0.583 |         0.559 |        0.574 |
| Median Parallax Coverage @ 24.0 WFD HealpixSlicer              |         0.555 |         0.579 |         0.555 |        0.57  |
| Median Parallax-DCR degeneracy @ 22.4 WFD HealpixSlicer        |         0.194 |         0.252 |         0.242 |        0.308 |
| Median Parallax-DCR degeneracy @ 24.0 WFD HealpixSlicer        |         0.19  |         0.252 |         0.235 |        0.306 |

# Proper Motion
|                                                            |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-----------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Proper Motion Error @ 20.5 All visits HealpixSlicer |         0.194 |         0.193 |         0.201 |        0.2   |
| Median Proper Motion Error @ 24.0 All visits HealpixSlicer |         1.993 |         2.022 |         2.15  |        2.137 |
| Median Proper Motion Error @ 20.5 WFD HealpixSlicer        |         0.194 |         0.193 |         0.201 |        0.2   |
| Median Proper Motion Error @ 24.0 WFD HealpixSlicer        |         1.994 |         2.023 |         2.151 |        2.137 |

# Rapid Revisit
|                                                      |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-----------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Area (sq deg) RapidRevisits All visits HealpixSlicer |       9533.08 |       9437.69 |       11578.2 |      20120.8 |
| Median RapidRevisits All visits HealpixSlicer        |          0    |          0    |           0   |          0   |
| RapidRevisits All visits HealpixSlicer               |      31568    |      31568    |       31568   |      31568   |
| Area (sq deg) RapidRevisits WFD HealpixSlicer        |       9482.12 |       9386.72 |       11527.3 |      20092   |
| Median RapidRevisits WFD HealpixSlicer               |          0    |          0    |           0   |          0   |
| RapidRevisits WFD HealpixSlicer                      |      31568    |      31568    |       31568   |      31568   |

# Fraction in Pairs
|                                                                          |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-------------------------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Fraction of visits in pairs (15-60 min) gri HealpixSlicer         |         0.884 |             0 |         0.932 |        0.935 |
| Median Fraction of visits in pairs (15-60 min) gri WFD+NES HealpixSlicer |         0.883 |             0 |         0.932 |        0.935 |

# Slews
|                            |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:---------------------------|--------------:|--------------:|--------------:|-------------:|
| Mean slewTime All visits   |         6.948 |         6.515 |         6.554 |        6.659 |
| Median slewTime All visits |         4.776 |         4.776 |         4.774 |        4.778 |
| Min slewTime All visits    |         2     |         2     |         2     |        2     |
| Max slewTime All visits    |       156     |       156     |       156     |      156     |

# Filter Changes
|                                                |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-----------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Filter Changes Whole Survey                    |     10464     |     10364     |      9583     |    10803     |
| Filter Changes Per Night OneDSlicer            |      3025     |      3025     |      3025     |     3025     |
| Max Filter Changes Per Night OneDSlicer        |        25     |        23     |        21     |       23     |
| Mean Filter Changes Per Night OneDSlicer       |         3.08  |         3.05  |         2.795 |        3.177 |
| Median Filter Changes Per Night OneDSlicer     |         2     |         2     |         2     |        2     |
| Min Filter Changes Per Night OneDSlicer        |         0     |         0     |         0     |        0     |
| N(+3Sigma) Filter Changes Per Night OneDSlicer |        59     |        64     |        66     |       63     |
| N(-3Sigma) Filter Changes Per Night OneDSlicer |         0     |         0     |         0     |        0     |
| Rms Filter Changes Per Night OneDSlicer        |         3.482 |         3.271 |         2.969 |        3.48  |

# Nvisits
|                                     |    pontus_2002 |    kraken_2044 |    mothra_2049 |     nexus_2097 |
|:------------------------------------|---------------:|---------------:|---------------:|---------------:|
| Fraction of total Nvisits All props |    1           |    1           |    1           |    1           |
| Nvisits All props                   |    2.42548e+06 |    2.45161e+06 |    2.44923e+06 |    2.44179e+06 |
| Median Nvisits All props OneDSlicer |  804           |  809           |  811           |  807           |
| Nvisits All props OneDSlicer        | 3025           | 3025           | 3025           | 3025           |

# Proposal Fractions
|                                                  |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Fraction of total Nvisits All props              |         1     |         1     |         1     |        1     |
| Fraction of total Nvisits WFD                    |         0.957 |         0.956 |         0.966 |        0.966 |
| Fraction of total Nvisits WideFastDeep           |         0.957 |         0.956 |         0.966 |        0.966 |
| Fraction of total Nvisits DeepDrillingCosmology1 |         0.043 |         0.045 |         0.034 |        0.034 |
| Fraction of total Nvisits DD                     |         0.043 |         0.045 |         0.034 |        0.034 |

# Median Nvisits WFD
|                                            |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:-------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median NVisits WFD u band HealpixSlicer    |            47 |            46 |            46 |           46 |
| Median NVisits WFD y band HealpixSlicer    |           142 |           142 |           143 |          147 |
| Median NVisits WFD z band HealpixSlicer    |           142 |           147 |           161 |          155 |
| Median NVisits WFD g band HealpixSlicer    |            66 |            67 |            65 |           64 |
| Median NVisits WFD all bands HealpixSlicer |           696 |           702 |           717 |          705 |
| Median NVisits WFD i band HealpixSlicer    |           150 |           151 |           149 |          149 |
| Median NVisits WFD r band HealpixSlicer    |           151 |           152 |           153 |          149 |

# Median CoaddM5 WFD
|                                         |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:----------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median CoaddM5 WFD u band HealpixSlicer |        25.453 |        25.453 |        25.383 |       25.408 |
| Median CoaddM5 WFD y band HealpixSlicer |        24.745 |        24.725 |        24.696 |       24.728 |
| Median CoaddM5 WFD z band HealpixSlicer |        25.569 |        25.586 |        25.572 |       25.585 |
| Median CoaddM5 WFD g band HealpixSlicer |        26.958 |        26.938 |        26.916 |       26.912 |
| Median CoaddM5 WFD i band HealpixSlicer |        26.455 |        26.466 |        26.413 |       26.437 |
| Median CoaddM5 WFD r band HealpixSlicer |        27.016 |        27.016 |        26.988 |       26.997 |

# Median FiveSigmaDepth
|                                                          |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:---------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Median fiveSigmaDepth WFD u band HealpixSlicer    |        23.283 |        23.292 |        23.235 |       23.241 |
| Median Median fiveSigmaDepth WFD y band HealpixSlicer    |        22.006 |        21.975 |        21.956 |       21.96  |
| Median Median fiveSigmaDepth WFD z band HealpixSlicer    |        22.785 |        22.798 |        22.729 |       22.747 |
| Median Median fiveSigmaDepth WFD g band HealpixSlicer    |        24.611 |        24.602 |        24.59  |       24.596 |
| Median Median fiveSigmaDepth WFD all bands HealpixSlicer |        23.457 |        23.452 |        23.389 |       23.386 |
| Median Median fiveSigmaDepth WFD i band HealpixSlicer    |        23.681 |        23.692 |        23.655 |       23.665 |
| Median Median fiveSigmaDepth WFD r band HealpixSlicer    |        24.236 |        24.24  |        24.221 |       24.232 |

# Median Internight Gap
|                                                           |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:----------------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Inter-Night Gap WFD u band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD u band HealpixSlicer    |        26.926 |        25.932 |         3.992 |        2.978 |
| Median Inter-Night Gap WFD y band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD y band HealpixSlicer    |         4.992 |         4.012 |         2.037 |        2.021 |
| Median Inter-Night Gap WFD z band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD z band HealpixSlicer    |        18.95  |         2.979 |         1.995 |        1.984 |
| Median Inter-Night Gap WFD g band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD g band HealpixSlicer    |        32.908 |        17.94  |        16.029 |       16.952 |
| Median Inter-Night Gap WFD all bands HealpixSlicer        |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD all bands HealpixSlicer |         1.994 |         1.057 |         1.014 |        1.014 |
| Median Inter-Night Gap WFD i band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD i band HealpixSlicer    |        13.438 |         6.484 |         6.009 |        6.454 |
| Median Inter-Night Gap WFD r band HealpixSlicer           |     31568     |     31568     |     31568     |    31568     |
| Median Median Inter-Night Gap WFD r band HealpixSlicer    |        13.967 |         3.999 |         3.983 |        3.971 |

# Median Airmass WFD
|                                                   |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:--------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Median airmass WFD u band HealpixSlicer    |         1.079 |         1.081 |         1.1   |        1.098 |
| Median Median airmass WFD y band HealpixSlicer    |         1.086 |         1.09  |         1.117 |        1.105 |
| Median Median airmass WFD z band HealpixSlicer    |         1.082 |         1.094 |         1.092 |        1.094 |
| Median Median airmass WFD g band HealpixSlicer    |         1.081 |         1.082 |         1.081 |        1.083 |
| Median Median airmass WFD all bands HealpixSlicer |         1.081 |         1.083 |         1.084 |        1.085 |
| Median Median airmass WFD i band HealpixSlicer    |         1.081 |         1.083 |         1.082 |        1.083 |
| Median Median airmass WFD r band HealpixSlicer    |         1.08  |         1.081 |         1.08  |        1.081 |

# Median Seeing WFD
|                                                     |   pontus_2002 |   kraken_2044 |   mothra_2049 |   nexus_2097 |
|:----------------------------------------------------|--------------:|--------------:|--------------:|-------------:|
| Median Median seeingEff WFD u band HealpixSlicer    |         0.979 |         0.968 |         0.996 |        0.993 |
| Median Median seeingEff WFD y band HealpixSlicer    |         0.802 |         0.82  |         0.837 |        0.822 |
| Median Median seeingEff WFD z band HealpixSlicer    |         0.816 |         0.817 |         0.842 |        0.842 |
| Median Median seeingEff WFD g band HealpixSlicer    |         0.92  |         0.921 |         0.926 |        0.924 |
| Median Median seeingEff WFD all bands HealpixSlicer |         0.84  |         0.844 |         0.867 |        0.851 |
| Median Median seeingEff WFD i band HealpixSlicer    |         0.833 |         0.828 |         0.854 |        0.837 |
| Median Median seeingEff WFD r band HealpixSlicer    |         0.865 |         0.866 |         0.881 |        0.872 |

# Skymap comparisons
- [Nvisits all bands](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_NVisits_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_NVisits_all_bands_HEAL_ComboSkyMap.png)
- [Nvisits alt/az all bands](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_Nvisits_as_function_of_Alt_Az_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Nvisits_as_function_of_Alt_Az_all_bands_HEAL_ComboSkyMap.png)
- [Median airmass all bands](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_Median_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Median_airmass_all_bands_HEAL_ComboSkyMap.png)
- [Max airmass all bands](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_Max_airmass_all_bands_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Max_airmass_all_bands_HEAL_ComboSkyMap.png)
- [CoaddM5 r band](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_CoaddM5_r_band_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_CoaddM5_r_band_HEAL_ComboSkyMap.png)
- [Normalized Proper Motion at 20.5](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_Normalized_Proper_Motion_@_20_5_All_visits_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Normalized_Proper_Motion_@_20_5_All_visits_HEAL_ComboSkyMap.png)
- [Normalized Parallax at 22.4](figures/nexus_2097_pontus_2002_mothra_2049_kraken_2044_Normalized_Parallax_@_22_4_All_visits_HEAL_ComboSkyMap.pdf)
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Normalized_Parallax_@_22_4_All_visits_HEAL_ComboSkyMap.png)
# Histogram comparisons
### CoaddM5 r band HealPix Histogram
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_CoaddM5_r_band_HEAL_ComboHistogram.png)
### Slew Distance Histogram
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Slew_Distance_Histogram_All_visits_ONED_ComboBinnedData.png)
### Zoom Slew Distance Histogram
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Zoom_Slew_Distance_Histogram_All_visits_ONED_ComboBinnedData.png)
### Slew Time Histogram
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Slew_Time_Histogram_All_visits_ONED_ComboBinnedData.png)
### Zoom Slew Time Histogram 
![png](figures/thumb.nexus_2097_pontus_2002_mothra_2049_kraken_2044_Zoom_Slew_Time_Histogram_All_visits_ONED_ComboBinnedData.png)
