# GeoDev Lab Africa Project

## Spatial Analysis of Primary Healthcare Accessibility in Anambra West, Anambra State

This repository documents my **GeoDev Lab Africa, Cohort One** learning journey and project work focused on using Geographic Information Systems (GIS) to understand spatial patterns in healthcare accessibility.

The project examines the relationship between **settlements, primary healthcare facilities, roads, administrative boundaries and spatial accessibility** in Anambra West Local Government Area (LGA), Anambra State, Nigeria.

## Project Overview

Access to healthcare is influenced not only by the number of health facilities available, but also by where those facilities are located relative to the communities they serve. This project applies geospatial data preparation, mapping and spatial analysis to investigate healthcare distribution and proximity across Anambra West.

The work progresses through a series of weekly deliverables covering:

- Study area mapping and project documentation
- Healthcare facility and settlement data collection
- Spatial data preparation and quality assessment
- Coordinate reference system (CRS) management
- Settlement-to-healthcare proximity analysis
- Documentation of datasets, sources and analytical decisions

## Study Area

**Anambra West LGA, Anambra State, Nigeria**

The analysis focuses on the spatial distribution of settlements and Primary Healthcare Centres (PHCs) within Anambra West.

## Repository Structure

```text
geodev-lab-project/
│
├── Week 1/
│   ├── Anambra West Map.png
│   ├── README.md
│   └── Settlement-Proximity-to-PHC-Brief_Anambra-West.md
│
├── Week 2/
│   ├── Week 2 Data Note.md
│   └── data_set/
│
├── Week 3/
│   └── Data Quality and Preparation Note.md
│
├── Week 4/
│   └── watsup.docx
│
└── README.md
```

## Weekly Progress

### Week 1: Study Area and Initial Spatial Analysis

The first stage established the project focus on **Primary Healthcare accessibility in Anambra West**. A study-area map and an initial project brief were prepared, with emphasis on understanding access inequalities, travel distance and factors affecting healthcare accessibility.

The initial spatial data was prepared for analysis by converting the original data from **EPSG:4326 (WGS 84)** to **EPSG:32632 (WGS 84 / UTM Zone 32N)**, clipping it to the study area and saving the analysis-ready data as a GeoPackage. fileciteturn6file0

### Week 2: Healthcare and Settlement Datasets

Week 2 focused on identifying and documenting the datasets required for the proximity analysis. The repository documents datasets for:

| Dataset | Source | Features | Geometry |
|---|---|---:|---|
| Anambra West LGA Boundary | QuickOSM | 1 | Polygon |
| Settlements | GRID3 | 16,706 | Multipolygon |
| Primary Healthcare Centres | GRID3 | 19 | Point |
| Roads | QuickOSM | 12 | Line |

The purpose was to assess how close settlements are to healthcare facilities and examine spatial patterns in healthcare distribution across the LGA. fileciteturn7file0

### Week 3: Data Quality and Preparation

The data preparation stage included:

- Reprojecting spatial data from **EPSG:4326 to EPSG:32632**
- Clipping data to the Anambra West study area
- Saving prepared data in **GeoPackage (`.gpkg`)** format
- Checking for duplicate features
- Checking geometry validity
- Checking spatial coverage
- Checking missing or empty attributes
- Verifying the CRS and spatial reference

The documented checks found no major data quality problems in the reviewed dataset. fileciteturn8file0

### Week 4: Continuing the GeoDev Lab Journey

The Week 4 folder is currently included as part of the project progression and will be updated as additional project work is documented.

## Data Sources

The project uses spatial datasets from sources including **GRID3** and **OpenStreetMap/QuickOSM**. The Week 2 documentation contains the source references used for the Anambra West boundary and population datasets. fileciteturn7file0

## Tools and Technologies

- **QGIS** for spatial data processing, mapping and analysis
- **OpenStreetMap / QuickOSM** for relevant geospatial datasets
- **GRID3** for population, settlement and health facility datasets
- **GeoPackage (`.gpkg`)** for analysis-ready spatial data
- **GitHub** for version control, documentation and project sharing

## Key Skills Demonstrated

This project demonstrates practical experience in:

- GIS data acquisition and management
- Spatial data cleaning and preparation
- Coordinate Reference Systems and reprojection
- Vector data processing
- Geometry and attribute quality checks
- Spatial proximity analysis
- Healthcare accessibility mapping
- Technical documentation
- Version control with GitHub

## Project Goal

The broader goal is to demonstrate how geospatial data can be transformed into useful spatial evidence for understanding **healthcare accessibility and distribution**. The project also serves as a practical record of developing GIS and spatial data analysis skills through the GeoDev Lab Africa programme.

## Author

**Ekwuocha Ngozi Jane**  
GIS Analyst | Environmental Management | Spatial Data & Geospatial Analysis

## Repository

[View the project on GitHub](https://github.com/Janny-Ngozi/geodev-lab-project)
