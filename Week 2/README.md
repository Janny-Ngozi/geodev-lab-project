# Week 2: Data Collection and Dataset Documentation

## GeoDev Lab Africa, Cohort One

**Project:** Spatial Analysis of Primary Healthcare Accessibility in Anambra West LGA, Anambra State, Nigeria

## Overview

Week 2 focused on identifying, collecting and documenting the spatial datasets required for the healthcare accessibility analysis.

The purpose was to bring together the core geographic layers needed to examine the relationship between healthcare facilities, settlements, roads, waterways and the administrative boundary of Anambra West LGA.

## Study Area

**Anambra West Local Government Area, Anambra State, Nigeria**

## Datasets

| Dataset | Source | Features | Key fields | Geometry |
|---|---|---:|---|---|
| Anambra West LGA Boundary | QuickOSM | 1 | full_id, name | Polygon |
| Settlements | GRID3 | 16,706 | full_id | Multipolygon |
| PHC facilities | GRID3 | 19 | fid, ward, facility name | Point |
| Roads | QuickOSM | 12 | fid | Line |
| Waterways | QuickOSM | Available in repository | Feature attributes | Line |

## Dataset Roles

**LGA Boundary:** Defines the geographic extent of the study and provides the boundary used to clip other datasets.

**Settlements:** Represents populated settlement areas that will be assessed in relation to healthcare facilities.

**PHC Facilities:** Provides the locations of healthcare facilities used in the accessibility analysis.

**Roads:** Provides transport-network information for later route-based accessibility analysis.

**Waterways:** Helps describe the riverine character of Anambra West and provides additional geographic context when interpreting accessibility.

## Data Sources

The project datasets were obtained from recognised geospatial data platforms, including GRID3 and OpenStreetMap through QuickOSM.

### GRID3

- [GRID3 Nigeria Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/explore)
- [GRID3 Nigeria Population](https://data.grid3.org/maps/GRID3::grid3-nga-population-v3-0/about)

### OpenStreetMap / QuickOSM

Relevant road and boundary data were obtained through OpenStreetMap using the QuickOSM plugin in QGIS.

## Repository Data

The collected spatial datasets are stored in the data_set folder as GeoPackage files:

- AW_LGA_Boundary.gpkg
- AW_Public_hospitals.gpkg
- AW_Road.gpkg
- AW_Settlement.gpkg
- AW_Settlement2.gpkg
- AW_Waterways.gpkg

## Initial Data Considerations

During dataset documentation, some attribute fields required attention during the data-quality and preparation stage. Examples included missing or incomplete descriptive fields such as road names and facility licence-status information.

These issues were documented rather than silently ignored, allowing the next stage of the project to address them where necessary.

## Week 2 Outcome

By the end of Week 2, the core datasets required for the project had been identified, collected and organised.

The project was ready to move into data quality assessment, CRS management, reprojection and spatial preparation in Week 3.

---

**Author:** Ekwuocha Ngozi Jane  
**Programme:** GeoDev Lab Africa, Cohort One
