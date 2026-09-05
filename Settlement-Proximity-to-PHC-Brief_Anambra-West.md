# Project Brief: Settlement Areas Proximity to Primary Health Care Centres (PHCs)
## Anambra West LGA, Anambra State, Nigeria

---

## 1. The Question

**Within Anambra West LGA, which settlements are close to — or effectively cut off from — a Primary Health Care Centre (PHC), and how does that access pattern change with the LGA's riverine, flood-prone geography?**

This narrows the earlier "hospitals to settlements" framing in two deliberate ways:

- **Facility tier:** Nigeria's health system runs on three tiers — primary, secondary, tertiary. PHCs are the designated first point of contact (routine care, immunization, maternal care, minor treatment); hospitals handle referral and emergency cases. For most rural communities, the PHC — not the general hospital — is the realistic day-to-day access point.
- **Geography:** Anambra West sits in the Lower Niger Basin and is described by its own LGA government as prone to annual seasonal flooding, with some communities relying on the Omambala/Niger river system rather than roads for transport. A proximity analysis here can't stop at dry-season distance.

---

## 2. Why It Matters

| Anambra West | Figure |
|---|---|
| LGA capital | Nzam |
| Area | ~584.1 km² |
| Population (2022 est.) | ~238,400 |
| Density | ~408.1/km² |

*(2022 figure is a Wikipedia/citypopulation.de estimate, not a fresh census count — cross-check against National Population Commission data before using in a formal deliverable.)*

- Anambra West is the largest and most sparsely populated of the Anambra LGAs looked at in this series so far — settlements are genuinely more spread out, which raises the stakes of getting the "nearest PHC" answer right.
- Anambra State's own health policy is organized around this exact tier: each of the state's 326 political wards has at least one PHC, while there are only about 20 secondary (general) hospitals statewide. That means for most Anambra West communities, the PHC *is* the health system in practical, daily terms — a gap here is a gap in basic care access, not just a gap in advanced care.
- Flooding is not a side note here — it's a defining feature of the LGA. A settlement that looks well-served by a PHC in the dry season may be effectively cut off for weeks during flood season, which a standard, one-time proximity map won't show.

---

## 3 & 4. The Data You Need — and Where It Comes From

| Data | What it gives you | Source | Link |
|---|---|---|---|
| PHC locations | Facility points with a level/type field you can filter to "Primary" | **GRID3 NGA – Health Facilities** (merges NHFR + GRID3 verification; classifies facilities as primary/secondary/tertiary) | https://data.grid3.org/search?tags=health+facilities |
| Anambra-specific facility extract | Pre-filtered Anambra State facility layer, useful as a starting point or cross-check | **Anambra Healthcare Facilities** (Dataphyte Dataplex, sourced from the national primary/secondary/tertiary facility dataset) | https://dataplex.dataphyte.com/products/anambra-healthcare-facilities |
| Facility cross-check | Independent list to validate the above against | **Nigeria: Hospitals and Clinics with registration status and Location** (Federal Ministry of Health, via HDX) | https://data.humdata.org/dataset/nigeria-hospitals-and-clinics-with-registration-status-and-location |
| Settlement locations | Settlement polygons + centroids (~100 m) with building counts | **GRID3 NGA – Settlement Extents** | https://data.grid3.org (search "Settlement Extents") |
| Population | Gridded population for demand-weighting | **WorldPop Nigeria** (Population Density & Counts) | https://hub.worldpop.org/ |
| Building footprints (supplementary) | Independent settlement-density check | **Microsoft Global ML Building Footprints** | https://github.com/microsoft/GlobalMLBuildingFootprints |
| Road network | For Phase 2+ travel-time analysis | **OpenStreetMap Nigeria**, via Geofabrik or HOT OSM | https://download.geofabrik.de/africa/nigeria.html or https://data.humdata.org/dataset/hotosm_nga_roads |
| Ward/LGA boundaries | To clip and aggregate to Anambra West and its wards | **GRID3 NGA – Operational LGA/Ward Boundaries** | https://grid3.org/geospatial-data-nigeria |
| Seasonal flood risk (for Phase 4) | To model which settlements lose access during flood season | **NIHSA Annual Flood Outlook** | https://nihsa.gov.ng/publications/ |

**A genuine data gap to flag early, not discover late:** OpenStreetMap's road tagging is sparse to non-existent for river/boat routes — the actual transport mode for parts of Anambra West. Standard road-network accessibility tools (like Network Analyst) are built for road tags, not waterways. This means the network-based phase of this project will likely need a documented workaround (e.g., manually digitizing known river transport routes, or treating riverine settlements as a separate category with a noted limitation) rather than a clean off-the-shelf solution.

---

## 5. What You Would Build

**Phase 1 — Ward-level PHC proximity (where you are now):**
Filter facility data to Primary level only, buffer by distance bands, overlay on GRID3 settlements, and aggregate to Anambra West's wards — since Anambra's own PHC planning is organized at the ward level, this makes your output directly comparable to how the state already thinks about coverage.

**Phase 2 — Network-based accessibility:**
Drive-time catchments using ArcGIS Network Analyst on the OSM road network, with the waterway limitation above documented rather than glossed over.

**Phase 3 — Weighted accessibility index:**
Two-Step Floating Catchment Area (2SFCA) method (Luo & Wang, 2003, *Environment and Planning B*, 30:865–884), weighing PHC capacity against the population it serves, rather than a binary in/out measure.

**Phase 4 — Seasonal access layer (this is the distinctive addition for Anambra West):**
Overlay NIHSA's seasonal flood risk classification against your Phase 2/3 results to produce **two accessibility pictures instead of one** — dry-season access and flood-season access — for the same settlements. This is the piece that turns a standard PHC-proximity study into something specific to Anambra West's real conditions.

**Final deliverable:** An ArcGIS Dashboard for Anambra West showing PHC accessibility per settlement/ward, with a toggle between dry-season and flood-season access, built so the same structure could later extend to other riverine LGAs (Anambra East, Ogbaru) facing similar conditions.

---

## 6. What Makes This Different From Ordinary Work

| Ordinary facility-proximity analysis | This project |
|---|---|
| All facility types lumped together | Filtered to the tier that actually matters for routine rural care (PHC) |
| One static access picture | Two: dry-season and flood-season access for the same settlements |
| Assumes roads are the only transport mode | Explicitly documents where road-based tools break down (riverine communities) instead of quietly ignoring it |
| Distance only | Population-weighted accessibility (2SFCA), not just presence/absence within a radius |
| Administrative units chosen for convenience | Aggregated to wards, matching Anambra State's own PHC planning structure |

---

*Brief prepared as a working document — verify population figures against National Population Commission data, and confirm current GRID3 dataset version numbers, before using this in a formal submission.*
