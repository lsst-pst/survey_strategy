### Potential runs to prepare for white paper call ###

Please note that this is a work in progress, a place to gather thoughts on what runs might be useful at the time of the call for white papers.

Baseline
  WFD with 18,000 sq deg footprint; NES; SCP + GP with 30 visits/filter; DD with 5 fields with u + grizy sequences.
  astro-lsst-01_2022 (baseline_2018a)

WFD only
  WFD with XX sq deg footprint, in pairs. 
 
GP at WFD cadence
  Similar to baseline, but remove GP proposal and just run WFD over the galactic plane range of RA.
  
Extra DD fields
  Similar to baseline, but increase the number of DD fields
  
DD fields with alternate cadence
  Similar to baseline, with 5(?) DD fields, but observed in only 3 filters each night, shorter gap between nights. 
  Rotate among the 3 filters being used.
  
Rolling cadence - dec bands
  Like baseline, but split sky into (2 or 3) bands of declination, observe the dec band every (2 or 3) years.
  
Rolling cadence - ra bands
  Like baseline, but observe blocks of RA in WFD 
  (split sky into 2 or 3 sections of RA and observe these bands every 2 or 3 years)
  
Rolling cadence - spherical harmonics
  Make spherical harmonics style masks and turn these on/off
  
Rolling cadence experiments - but all on/off vs. leave some percent of the background WFD "on"

Pairs in the same filter, vs. pairs in different filters. 

Single visits in a night.

Triple visits in a night.

TOO visits - X triggers per year, to search ? fields around a given field location to ? depth in ? filter

Any other runs from https://github.com/LSSTScienceCollaborations/ObservingStrategy/tree/master/opsim?
