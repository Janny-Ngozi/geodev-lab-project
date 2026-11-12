import csv


with open("wards.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ward_name = row["ward"]
        area_km2 = float(row["area_km2"])
        area_hectares = area_km2 * 100

        if area_km2 > 9:
            size = "large"
        else:
            size = "small"

        print(f"{ward_name} is {area_hectares:g} hectares and is a {size} ward")
