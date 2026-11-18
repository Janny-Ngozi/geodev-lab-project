from pathlib import Path

import pandas as pd

data_path = Path(r"C:\Users\jane\Documents\geodev-lab-project\Month_1\Week 2\data_set\AW_Processed\AW_Ward pop.csv")
pop = pd.read_csv(data_path)

print(pop.head())
print("shape:", pop.shape)
print("columns:", list(pop.columns))
print(pop.dtypes)

pop["Population"] = (
    pop["Population"]
    .astype("string")
    .str.replace(",", "", regex=False)
)
pop["Population"] = pd.to_numeric(pop["Population"], errors="coerce")
print(pop["Population"].describe())
