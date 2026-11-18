import pandas as pd
from pathlib import Path

csv_path = Path(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Ward pop.csv")
pop = pd.read_csv(csv_path)

pop["Population"] = pd.to_numeric(
    pop["Population"].astype("string").str.replace(",", "", regex=False),
    errors="coerce",
)
pop = pop.dropna(subset=["Population"])

big = pop[pop["Population"] > 10000]
print(big)
print("wards over 10,000:", len(big))

ranked = pop.sort_values("Population", ascending=False)
print(ranked.head())

pop["population_thousands"] = pop["Population"] / 1000
print(pop.head(3))
print("Total population:", pop["Population"].sum())