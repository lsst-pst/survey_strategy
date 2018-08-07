| Run name                        | HA bonus      | HA max| X bonus | Python | dome crawl | New OL correction  | Note                                                         |
| --------------------------------|:-------------:|:-----:|:------: |:------:|:----------:| :----------------: | :-----------:                                                |
| [baseline2018a](#baseline2018a) | 0.3           | 3.0   | 0.0     | 2      |     no     | no                 | Current opsimv4 baseline                                     |
| [kraken_2026](#kraken_2026)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Python 3 baseline2018a replacement (with dome crawl and OL)  |
| [colossus_2665](#colossus_2665) | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Python 3 baseline2018a replacement (with dome crawl and OL), WFD area increased by 1.5 degrees north an south  |
| [pontus_2002](#pontus_2002)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey                        |
| [colossus_2664](#colossus_2664) | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | WFD cadence in GP. GP proposal turned off                                                  |
| [colossus_2667](#colossus_2667) | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Single visits per night survey                                                                            |
| [pontus_2489](#pontus_2489)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | "Many visits" 20s visits with single snap, 40s visits in u band                         |
| [kraken_2035](#kraken_2035])    | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | 9 Deep Drilling Fields (DDFs), 4 already decided + 5 additional                            |
| [mothra_2045](#mothra_2045)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | 2 alternating Dec bands switched every other year, WFD off                                 |
| [pontus_2502](#pontus_2502)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | 2 alternating Dec bands switched every other year, WFD on at 25% level                     |
| [kraken_2036](#kraken_2036)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Full WFD first and last 2 years, 3 alternating dec bands in between                        |
| [kraken_2042](#kraken_2042)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Single 30 second snaps in all filters                        |
| [kraken_2044](#kraken_2044)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey, no pairs             |
| [mothra_2049](#mothra_2049)     | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey, 2 alternating Dec bands switched every other year              |
| [nexus_2097](#nexus_2097)       | 0.3           | 3.0   | 0.0     | 3      |     yes    | yes                | Simulation of a PanSTARRs like survey, Full WFD first and last 2 years, 3 alternating dec bands in between              |


# Simulations

## Creating a new baseline with latest code, dome crawl, and OL correction delay

### `baseline2018a`
- current opsimv4 baseline
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018a/config_run)

### `kraken_2026`
- recreation of baseline using Python3 code, dome crawl, and new delay for OL correction
- most likely new baseline
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_dc_cl/config_run)
- [comparison with baseline2018a](baseline2018a_kraken2026_comp/README.md)
- [dither comparison with baseline2018a](baseline2018a_kraken2026_comp_dither/README.md)
- [comparison with pontus_2003](pontus_2003_kraken2026_comp/README.md)


## Alternate survey strategies

### `colossus_2665`
- WFD minimum and maximum dec limits increased by 1.5 degrees
- possible new baseline
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/baseline2018_dc_cl_wfd15/config_run)
- [comparison with baseline2018a](baseline2018a_colossus2665_comp/README.md)
- [comparison with kraken_2026](kraken2026_colossus2665_comp/README.md)
- [dither comparison with kraken_2026](kraken2026_colossus2665_comp_dither/README.md)

### `pontus_2002`
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DecMin = -78, DecMax = +18)
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_big_wfdonly/config_run)
- [comparison with baseline2018a](baseline2018a_pontus2002_comp/README.md)
- [comparison with kraken_2026](kraken2026_pontus2002_comp/README.md)
- [dither comparison with kraken_2026](kraken2026_pontus2002_comp_dither/README.md)

### `colossus_2664`
- WFD through GP
- GP turned off
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_nogp/config_run)
- [comparison with baseline2018a](baseline2018a_colossus2664_comp/README.md)
- [comparison with kraken_2026](kraken2026_colossus2664_comp/README.md)
- [dither comparison with kraken_2026](kraken2026_colossus2664_comp_dither/README.md)

### `colossus_2667`
- single visits per night survey
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_nopairs/config_run)
- [comparison with baseline2018a](baseline2018a_colossus2667_comp/README.md)
- [comparison with kraken_2026](kraken2026_colossus2667_comp/README.md)
- [dither comparison with kraken_2026](kraken2026_colossus2667_comp_dither/README.md)

### `pontus_2489`
- "Many visits" survey
-  20s visits with single snap in `g,r,i,z,y`
-  40s visits with single snap in `u` band
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_manyvisits/config_run)
- [comparison with baseline2018a](baseline2018a_pontus2489_comp/README.md)
- [comparison with kraken_2026](kraken2026_pontus2489_comp/README.md)

### `kraken_2035`
- 9 DDFs
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_9ddfs)
- [comparison with baseline2018a](baseline2018a_kraken2035_comp/README.md)
- [comparison with kraken_2026](kraken2026_kraken2035_comp/README.md)

### `kraken_2042`
- Single 30 second snaps in all bands
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_single_snaps_30sec/config_run)
- [comparison with kraken_2026](kraken2026_kraken2042_comp/README.md)

### `kraken_2044`
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DecMin = -78, DecMax = +18)
- No pairs
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_bigwfd_nopairs/config_run)
- [comparison with kraken_2026](kraken2026_kraken2044_comp/README.md)
- [comparison with pontus_2002](pontus2002_kraken2044_comp/README.md)
- [comparison with pontus_2002, mothra_2049, and nexus_2097](pontus2002_kraken2044_mothra2049_nexus2097_comp/README.md)


## Rolling cadences

### `mothra_2045`
- Rolling cadence
- 2 alternating Dec bands switched every other year
- No WFD proposal in the background.
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_2rolling_decbands/config_run)
- [comparison with baseline2018a](baseline2018a_mothra2045_comp/README.md)
- [comparison with kraken_2026](kraken2026_mothra2045_comp/README.md)

### `pontus_2502`
- Rolling cadence
- 2 alternating Dec bands switched every other year
- WFD proposal in the background at 25% level.
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_2rolling_decbands_wfdbg25p/config_run)
- [comparison with kraken_2026](kraken2026_pontus2502_comp/README.md)

### `kraken_2036`
- Rolling cadence
- Full WFD first and last 2 years, 3 alternating dec bands in between
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018a_3rolling_decbands_single_prop/config_run)
- [comparison with kraken_2026](kraken2026_kraken2036_comp/README.md)

### `mothra_2049`
- Rolling cadence
- 2 alternating Dec bands switched every other year
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DecMin = -78, DecMax = +18)
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_bigwfd_2rolling_dec/config_run)
- [comparison with kraken_2026](kraken2026_mothra2049_comp/README.md)
- [comparison with pontus_2002](pontus2002_mothra2049_comp/README.md)

### `nexus_2097`
- Rolling cadence
- Full WFD first and last 2 years, 3 alternating dec bands in between
- Simulation of a PanSTARRs like survey
- WFD + DD WFD having 274000 deg sq (X<1.5, DecMin = -78, DecMax = +18)
- [configuration repository](https://github.com/lsst-ts/opsim4_config/tree/whitepaper2018_bigwfd_3rolling_dec/config_run)
- [comparison with kraken_2026](kraken2026_nexus2097_comp/README.md)
- [comparison with pontus_2002](pontus2002_nexus2097_comp/README.md)
