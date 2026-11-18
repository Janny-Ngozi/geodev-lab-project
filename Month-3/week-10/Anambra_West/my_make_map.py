import geopandas as gpd
import matplotlib.pyplot as plt
from pathlib import Path

script_dir = Path(__file__).parent
processed_data_dir = Path(
    r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed"
)
facilities_path = script_dir / "data" / "processed" / "health_facilities.gpkg"

wards = gpd.read_file(processed_data_dir / "AW_Wards.gpkg", layer="AW_Wards")
facilities = gpd.read_file(facilities_path, layer="facilities").to_crs(wards.crs)

fig, ax = plt.subplots(figsize=(7, 8))
wards.plot(ax=ax, color="#E6F2F3", edgecolor="#037E8E")
facilities.plot(ax=ax, color="#094923", markersize=18)
ax.set_title("Health Facilities in Anambra West LGA")
ax.set_axis_off()

output_path = script_dir / "anambra_west_facilities_map.png"
fig.savefig(output_path, dpi=150, bbox_inches="tight")
print("Map saved to", output_path)
