from pathlib import Path

import pandas as pd

data_path = Path(__file__).parent / "data" / "raw" / "ward_population.csv"
pop = pd.read_csv(data_path)

print(pop.head())
print("shape:", pop.shape)
print("columns:", list(pop.columns))
print(pop.dtypes)
print(pop["population_2024"].describe())
