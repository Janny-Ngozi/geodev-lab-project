import pandas as pd
import geopandas as gpd

wards = gpd.read_file(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Wards.gpkg", layer="AW_Wards")
pop = pd.read_csv(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Ward pop.csv")

pop["Population"] = pd.to_numeric(
    pop["Population"].astype("string").str.replace(",", "", regex=False),
    errors="coerce",
)
pop = pop.dropna(subset=["Ward", "Population"]).copy()

def clean_name(name):
    if pd.isna(name):
        return ""
    return "".join(char for char in str(name).upper() if char.isalnum())

csv_to_boundary_ward = {
    "Umuoba-Anam": "Abegbu/Iyiora",
    "Ifite-Anam": "Mmiata",
    "Umuenwelum-Anam": "Umuem",
}
pop["join_name"] = pop["Ward"].replace(csv_to_boundary_ward)
pop["join_key"] = pop["join_name"].apply(clean_name)

ward_aliases = wards[["ward", "ward_alt_n"]].copy()
ward_aliases["name"] = ward_aliases["ward_alt_n"].fillna("").str.split(",")
ward_aliases = ward_aliases.explode("name")
ward_aliases = pd.concat(
    [
        wards[["ward"]].assign(name=wards["ward"]),
        ward_aliases[["ward", "name"]],
    ],
    ignore_index=True,
)
ward_aliases["join_key"] = ward_aliases["name"].apply(clean_name)

matched_names = ward_aliases.merge(pop, on="join_key", how="inner")
joined = wards.merge(
    matched_names[["ward", "Ward", "Population"]].drop_duplicates(),
    on="ward",
    how="left",
)

matched = joined["Population"].notna().sum()
print("Matched wards:", matched, "of", len(wards))
print(joined[["ward", "Ward", "Population"]])
print("Unmatched boundary wards:", joined.loc[joined["Population"].isna(), "ward"].tolist())
matched_csv_names = set(matched_names["Ward"])
print("Unmatched CSV ward names:", pop.loc[~pop["Ward"].isin(matched_csv_names), "Ward"].tolist())