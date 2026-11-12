# Project Brief: Settlement Areas Proximity to Primary Health Care Centres (PHCs)
## Anambra West LGA, Anambra State, Nigeria

---

## 1. The Question

**Within Anambra West LGA, which settlements are close to or effectively cut off from a Primary Health Care Centre (PHC), and how does that access pattern change with the LGA's riverine and flood prone geography?**

This narrows the earlier "hospitals to settlements" framing in two deliberate ways:

- **Facility tier:** Nigeria's health system operates across three tiers: primary, secondary and tertiary. PHCs are the designated first point of contact for routine care, immunisation, maternal care and minor treatment. Hospitals handle referral and emergency cases. For most rural communities, the PHC, rather than the general hospital, is the realistic day to day access point.
- **Geography:** Anambra West sits in the Lower Niger Basin and is described by its own LGA government as prone to annual seasonal flooding. Some communities rely on the Omambala and Niger river systems rather than roads for transport. A proximity analysis in this setting should therefore consider more than dry season distance.

---

## 2. Why It Matters

| Anambra West | Figure |
|---|---|
| LGA capital | Nzam |
| Area | Approximately 584.1 km² |
| Population (2022 estimate) | Approximately 238,400 |
| Density | Approximately 408.1/km² |

*(2022 Wikipedia and City Population estimate.)*

- Anambra West is the largest and most sparsely populated of the Anambra LGAs considered in this series so far. Settlements are more widely dispersed, which increases the importance of identifying the nearest PHC accurately.
- Anambra State's health policy is organised around this tier. Each of the state's 326 political wards has at least one PHC, while there are only about 20 secondary general hospitals statewide. For most communities in Anambra West, the PHC is the practical point of access to routine healthcare. Limited access therefore represents a gap in basic healthcare provision, not only a gap in advanced care.
- Flooding is a defining feature of the LGA. A settlement that appears to have good access to a PHC during the dry season may become difficult to reach for weeks during flood season. A standard one time proximity map may not capture this change.

---

## 3 and 4. The Data Needed and Where It Comes From

| Data | What it gives you | Source | Link |
|---|---|---|---|
| PHC locations | Facility points with a level or type field that can be filtered to "Primary" | **GRID3 NGA: Health Facilities** (combines NHFR and GRID3 verification and classifies facilities as primary, secondary or tertiary) | https://data.grid3.org/search?tags=health+facilities |
| Anambra specific facility extract | Pre filtered Anambra State facility layer that can be used as a starting point or cross check | **Anambra Healthcare Facilities** (Dataphyte Dataplex, sourced from the national primary, secondary and tertiary facility dataset) | https://dataplex.dataphyte.com/products/anambra-healthcare-facilities |
| Facility cross check | Independent list for validating the above data | **Nigeria: Hospitals and Clinics with registration status and Location** (Federal Ministry of Health, via HDX) | https://data.humdata.org/dataset/nigeria-hospitals-and-clinics-with-registration-status-and-location |
| Settlement locations | Settlement polygons and centroids of approximately 100 m, with building counts | **GRID3 NGA: Settlement Extents** | https://data.grid3.org (search "Settlement Extents") |
| Population | Gridded population data for demand weighting | **WorldPop Nigeria** (Population Density and Counts) | https://hub.worldpop.org/ |
| Building footprints (supplementary) | Independent settlement density check | **Microsoft Global ML Building Footprints** | https://github.com/microsoft/GlobalMLBuildingFootprints |
| Road network | Data for Phase 2 and later travel time analysis | **OpenStreetMap Nigeria**, via Geofabrik or HOT OSM | https://download.geofabrik.de/africa/nigeria.html or https://data.humdata.org/dataset/hotosm_nga_roads |
| Ward and LGA boundaries | Data for clipping and aggregating results to Anambra West and its wards | **GRID3 NGA: Operational LGA and Ward Boundaries** | https://grid3.org/geospatial-data-nigeria |
| Seasonal flood risk (for Phase 4) | Data for modelling which settlements may lose access during flood season | **NIHSA Annual Flood Outlook** | https://nihsa.gov.ng/publications/ |

---

## 5. What Makes This Different From Ordinary Work

| Ordinary facility proximity analysis | This project |
|---|---|
| All facility types are grouped together | Facilities are filtered to the tier that matters for routine rural care, which is the PHC |
| One static access picture | Two access scenarios are considered: dry season and flood season |
| Roads are assumed to be the only transport mode | The analysis documents where road based methods may not work well for riverine communities instead of ignoring the limitation |
| Distance is the only measure | Population weighted accessibility using the 2SFCA method is considered, rather than only measuring presence or absence within a radius |
| Administrative units are selected for convenience | Results are aggregated to wards, matching Anambra State's PHC planning structure |
