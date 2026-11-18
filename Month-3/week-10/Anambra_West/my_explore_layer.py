import geopandas as gpd
from pathlib import Path

gpkg_path = Path(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Wards.gpkg")
print(gpd.list_layers(gpkg_path))
wards = gpd.read_file(gpkg_path, layer="AW_Wards")


print(wards.head())
print("Rows and columns:", wards.shape)
print(wards.geom_type.value_counts())
print("CRS:", wards.crs)
print("Bounds:", wards.total_bounds)