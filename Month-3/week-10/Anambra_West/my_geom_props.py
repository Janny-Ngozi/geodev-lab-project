import geopandas as gpd

wards = gpd.read_file(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Wards.gpkg", layer="AW_Wards")
first = wards.geometry.iloc[0]
print(type(first))
print(first)
print("valid :", first.is_valid)
print("centroid :", first.centroid)