import pandas as pd
from pathlib import Path

csv_path = Path(__file__).parent / "data" / "raw" / "ward_population.csv"
pop = pd.read_csv(csv_path)

big = pop[pop["population_2024"] > 35000]
print(big)
print("wards over 35,000:", len(big))

ranked = pop.sort_values("population_2024", ascending=False)
print(ranked.head())

pop["population_thousands"] = pop["population_2024"] / 1000
print(pop.head(3))
print("Total population:", pop["population_2024"].sum())