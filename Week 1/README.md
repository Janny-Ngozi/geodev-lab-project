# My GeoDev-Lab-Africa-project
A spatial view and analysis into the Primary Health care accessibility in Anambra West, Anambra State.
A deep dive into access inequalities, travel time and causes.
Built over 12 months with GeoDev Lab Africa, Corhort One
See project-brief.md for the full brief

# Data Quality and Preparation Note

## Study Area

**Location:** Anambra West, Anambra State, Nigeria

## CRS and Data Preparation

The original dataset was in **EPSG:4326 (WGS 84 geographic coordinate system)**. The data was reprojected to **EPSG:32632 (WGS 84 / UTM Zone 32N)** because the study area falls within UTM Zone 32N and the projected CRS uses **metres**, making it suitable for distance and area measurements.

The following data preparation steps were carried out:

* Reprojected the original Shapefile from **EPSG:4326 to EPSG:32632**.
* Clipped the data to the **Anambra West study area boundary**.
* Saved the analysis-ready dataset as a **GeoPackage (`.gpkg`)**.

## Five Data Quality Checks

| Quality Check                    | Result                                                                                     | Action Taken        |
| -------------------------------- | ------------------------------------------------------------------------------------------ | ------------------- |
| **1. Duplicate features**        | No duplicate features were identified.                                                     | No action required. |
| **2. Geometry validity**         | All geometries were valid with no self-intersections or invalid shapes identified.         | No action required. |
| **3. Spatial coverage**          | The dataset provides coverage across the required study area after clipping.               | No action required. |
| **4. Missing/empty attributes**  | No significant missing or empty attribute values were found.                               | No action required. |
| **5. CRS and spatial reference** | The data was successfully reprojected to **EPSG:32632** and the CRS was correctly defined. | No action required. |

## Problems Identified

No major data quality problems were identified during the checks. The dataset passed all five quality checks, so no corrections or fixes were required.

## Analysis-Ready File

The cleaned, clipped, and reprojected analysis-ready dataset is stored as:

`data/anambra_west_reprojected.gpkg`

The file contains the prepared spatial data in **EPSG:32632** and is ready for further spatial analysis.
