import geopandas as gpd
from pathlib import Path

script_dir = Path(__file__).parent
data_dir = script_dir / "data" / "processed"
output_gpkg = data_dir / "week10_outputs.gpkg"

wards = gpd.read_file(data_dir / "wards.gpkg", layer="wards")
wards.to_file(output_gpkg, layer="wards_copy")
wards.drop(columns="geometry").to_csv(script_dir / "wards_table.csv", index=False)
print(gpd.list_layers(output_gpkg))
