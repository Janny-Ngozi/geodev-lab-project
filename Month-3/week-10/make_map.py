import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

script_dir = Path(__file__).parent
data_dir = script_dir / "data" / "processed"

wards = gpd.read_file(data_dir / "wards.gpkg", layer="wards")
facilities = gpd.read_file(data_dir / "health_facilities.gpkg", layer="facilities")

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health Facilities in Ibadan North LGA")
ax.set_axis_off()

fig.savefig(script_dir / "ibadan_facilities_map.png", dpi=150, bbox_inches="tight")
print("Map saved")
