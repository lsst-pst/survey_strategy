## Links to documents or resources in other locations.

### LSST docs

The [LSST Overview paper](https://www.lsst.org/content/lsst-science-drivers-reference-design-and-anticipated-data-products) provides a short summary of the four primary science drivers, as well as the expected performance of LSST in terms of throughputs, and calibration. Also relevant for the purposes of survey strategy, there are discussions on survey constraints and tradeoffs in this paper. 

The [LSST SRD](http://ls.st/srd) (Science Requirement Document) describes the official requirements for LSST science deliverables. Section 3.4 is the most relevant for survey strategy, although other sections are relevant for telescope and camera performance such as throughputs and readout time. The top-level requirements in section 3.4 have been translated to MAF metrics which are run on every simulated survey.

The [LSST DPDD](http://ls.st/dpdd) (Data Products Definition Document) describes the data products that LSST will provide, with some high-level background on how they will be produced. If you want to know what will be contained in various catalogs, this is a good place to look. 

[LDM-151](http://ls.st/ldm-151) (LSST Data Management Science Pipelines Design document) describes the LSST data management processing pipelines. This provides details of how and when images will be processed and catalogs will be generated, including information on the algorithms used in each processing stage. If you want to know more about the details of a value in an output catalog and how it will be calculated, this is the place to look. 

The [LSST DMSR](http://ls.st/lse-61) (Data Management System Requirements) document details the official requirements for LSST's data management processing. This is a higher level of detail than the DPDD on the characteristics and specifications of individual data products but does not describe how these data products are created. This is more useful to DM than to the public.

### Community

The [Observing Strategy White Paper](https://github.com/LSSTScienceCollaborations/ObservingStrategy) (OSWP) is a community-driven paper describing a wide variety of science cases and their implications for survey strategy. This paper is primarily aimed at helping define the main (90\%) WideFastDeep survey.

The 2011 community-contributed Deep Drilling white papers are available and some other DD related information and links are available on the LSST.org [DD page](https://www.lsst.org/scientists/survey-design/ddf). 

### Scheduler

A description of the [opsim v4 output database](https://lsst-sims.github.io/sims_ocs/database.html).

These links below may not be that useful to the general public, but are useful resources while working on implementing new scheduler software (such as the feature-based scheduler). 

Survey Strategy Notes from Tiago on [confluence](https://confluence.lsstcorp.org/display/LTS/Survey+Strategy+-+Tiago+Ribeiro)

Scheduler release [plan](https://confluence.lsstcorp.org/pages/viewpage.action?pageId=41781661)  (needs to be updated) <br>
Another view of planned scheduler [capabilities](https://confluence.lsstcorp.org/display/SIM/SOCS-Scheduler+Capabilities)

The [LSST scheduler requirements](https://docushare.lsst.org/docushare/dsweb/Get/LTS-347/Scheduler%20Requirements%20v4.2.1.pdf) document (LTS-347) describe the detailed requirements for the scheduling software. 

The [LSST OCS-scheduler design](https://docushare.lsst.org/docushare/dsweb/Get/LTS-226/LTS226-SchedulerDesign-1.1.pdf) document (LTS-226) describes additional requirements and design considerations for the OCS and scheduler software. 

The [2016 Scheduler SPIE](https://docushare.lsstcorp.org/docushare/dsweb/Get/Publication-131/) paper describes the development of the scheduler in opsim v4, while the [2016 SOCS SPIE](https://docushare.lsstcorp.org/docushare/dsweb/Get/Publication-116/) paper describes the development of the simulated OCS in opsim v4.
