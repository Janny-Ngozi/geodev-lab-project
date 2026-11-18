import pandas as pd
import geopandas as gpd
from pathlib import Path

csv_path = Path(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_PHC.csv")
table = pd.read_csv(csv_path)
print(table.head(3))

table["longitude"] = pd.to_numeric(table["longitude"], errors="coerce")
table["latitude"] = pd.to_numeric(table["latitude"], errors="coerce")
table = table.dropna(subset=["longitude", "latitude"])

facilities = gpd.GeoDataFrame(
    table,
    geometry=gpd.points_from_xy(table["longitude"], table["latitude"]),
    crs="EPSG:4326",
)
print(facilities.head(3))
print(facilities.crs)

output_dir = Path(__file__).parent / "data" / "processed"
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / "health_facilities.gpkg"

facilities.to_file(output_path, layer="facilities", driver="GPKG")
print("Saved", len(facilities), "facilities to", output_path)

                   