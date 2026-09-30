# Week 3: Data Quality Assessment and Spatial Preparation

## GeoDev Lab Africa, Cohort One

**Project:** Spatial Analysis of Primary Healthcare Accessibility in Anambra West LGA, Anambra State, Nigeria

## Overview

Week 3 focused on preparing the spatial datasets for analysis and checking whether they were suitable for subsequent GIS operations.

The main tasks were Coordinate Reference System (CRS) management, reprojection, clipping and data-quality checks.

## Study Area

**Anambra West Local Government Area, Anambra State, Nigeria**

## Coordinate Reference System

The source spatial data was initially provided in:

**EPSG:4326 - WGS 84**

EPSG:4326 is a geographic coordinate system whose coordinates are expressed in degrees.

For distance and area-based analysis, the data was reprojected to:

**EPSG:32632 - WGS 84 / UTM Zone 32N**

This projected CRS uses metres as its unit, making it more appropriate for measurements such as distance and area within the study area.

## Data Preparation Workflow

1. Reviewed the source CRS.
2. Reprojected the spatial data from EPSG:4326 to EPSG:32632.
3. Clipped the relevant data to the Anambra West LGA boundary.
4. Checked the resulting geometries and attributes.
5. Saved the prepared spatial data in GeoPackage (.gpkg) format.
6. Confirmed that the prepared data was suitable for subsequent spatial analysis.

## Data Quality Checks

| Quality Check | Result | Action |
|---|---|---|
| Duplicate features | No duplicate features identified | No correction required |
| Geometry validity | Geometries were valid | No correction required |
| Spatial coverage | Required study area was covered after clipping | No correction required |
| Missing/empty attributes | No significant missing or empty values identified in the reviewed data | No correction required |
| CRS and spatial reference | Data successfully reprojected to EPSG:32632 | No correction required |

## Why These Checks Matter

**Duplicate features:** Duplicate features can cause features to be counted more than once and distort subsequent analysis.

**Geometry validity:** Invalid geometries can cause errors or unexpected results during spatial operations such as intersections, buffers and joins.

**Spatial coverage:** The datasets must cover the intended study area so communities or facilities are not unintentionally excluded.

**Missing attributes:** Important missing attributes can limit filtering, classification and interpretation.

**CRS:** Using an unsuitable CRS can produce incorrect distance and area measurements. A projected CRS using metres is therefore important for the planned accessibility analysis.

## Problems Identified

No major data-quality problems were identified during the documented checks.

The reviewed data passed the five quality checks, so no major corrective action was required.

## Analysis-Ready Data

The prepared datasets are stored in the Week 2 data_set folder as GeoPackage files.

## Week 3 Outcome

At the end of Week 3, the project datasets had been reviewed, reprojected and prepared for spatial analysis.

The project was ready to progress from data preparation to actual spatial analysis, including settlement-to-PHC proximity and accessibility assessment.

---

**Author:** Ekwuocha Ngozi Jane  
**Programme:** GeoDev Lab Africa, Cohort One
