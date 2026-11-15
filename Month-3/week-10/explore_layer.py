import geopandas as gpd
from pathlib import Path

gpkg_path = Path(__file__).parent / "data" / "processed" / "wards.gpkg"
print(gpd.list_layers(gpkg_path))
wards = gpd.read_file(gpkg_path, layer="wards")


print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)