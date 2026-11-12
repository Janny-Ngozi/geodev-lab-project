import argparse
import csv
from pathlib import Path


def inspect_column(rows, column):
    """Return a summary of the numeric values in one CSV column."""
    values = []

    for row in rows:
        raw = (row.get(column) or "").strip()
        if not raw:
            continue

        try:
            values.append(float(raw))
        except ValueError:
            continue

    if not values:
        raise ValueError(f"No numeric values found in column: {column}")

    return {
        "smallest": min(values),
        "largest": max(values),
        "count": len(values),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Print a summary of two numeric columns in a CSV file."
    )
    parser.add_argument(
        "csv_file",
        nargs="?",
        default="AW_PHC.csv",
        type=Path,
        help="CSV file to inspect (default: AW_PHC.csv)",
    )
    args = parser.parse_args()

    with args.csv_file.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        columns = reader.fieldnames or []

    print("Number of rows:", len(rows))
    print("Columns:", columns)

    for column in ("longitude", "latitude"):
        if column not in columns:
            raise SystemExit(f"Required column '{column}' was not found in {args.csv_file}")

    longitude_results = inspect_column(rows, "longitude")
    latitude_results = inspect_column(rows, "latitude")

    print("Longitude results:", longitude_results)
    print("Latitude results:", latitude_results)


if __name__ == "__main__":
    main()
