### Potential runs to prepare for white paper call ###

Please note that this is a work in progress, a place to gather thoughts on what runs might be useful at the time of the call for white papers.

Current official baseline
  WFD with 18,000 sq deg footprint; NES; SCP + GP with 30 visits/filter; DD with 5 fields with u + grizy sequences.
  astro-lsst-01_2022 (baseline2018a)

Likely next baseline run
  Same as above, but with dome crawl turned on and WFD extended by 1.5deg N and S to meet SRD area requirements after dithering. (colossus_2665)

WFD + DD
  WFD having 274000 deg sq (X<1.5, DeMin = -78, DecMax = +18) (pontus_2002)
   
"Many visits"
  20s visits with single snap, 40s visits in u band (pontus_2489)
  
GP at WFD cadence
  Similar to baseline, but remove GP proposal and just run WFD over the galactic plane range of RA. (colossus_2664)

Single visits in a night. (colossus_2667)
  
Extra DD fields
  Similar to baseline, but increase the number of DD fields (kraken_2035)
    
Rolling cadence - dec bands
  Like baseline, but split sky into (2 or 3) bands of declination, observe the dec band every (2 or 3) years. (mothra_2045, pontus_2502, kraken_2036)
  


Potential runs TBD:

Pairs in different filters.

Rolling cadence - spherical harmonics
  Make spherical harmonics style masks and turn these on/off (to be done with FBS, but not for end of June). 
  
Rolling cadence experiments - but all on/off vs. leave some percent of the background WFD "on".

Triple visits in a night.

DD fields with alternate cadence,
  Similar to baseline, with 5(?) DD fields, but observed in only 3 filters each night, shorter gap between nights. 
  Rotate among the 3 filters being used.  

Any other runs from https://github.com/LSSTScienceCollaborations/ObservingStrategy/tree/master/opsim
