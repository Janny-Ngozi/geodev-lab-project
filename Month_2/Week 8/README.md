# Week 8: Inspecting CSV Data

This practical uses `AW_PHC.csv`, a small dataset of 19 healthcare facility records in Anambra West, Anambra State.

## Files

- `inspect_data.py`: reads a CSV file and summarises numeric columns.
- `AW_PHC.csv`: the dataset used for the exercise.
- `Screenshots/`: add the required `week8.png` screenshot here.

## Run the script

Open a terminal in this folder and run:

```powershell
uv run inspect_data.py
```

The script defaults to `AW_PHC.csv` and prints the row count, column names and summary dictionaries for the `longitude` and `latitude` columns. You can also provide another CSV filename as an argument.

## Data note

The CSV contains public healthcare facility information. The copy included here is limited to the small dataset used for this learning exercise. Check any dataset before sharing it publicly and remove personal or sensitive information where applicable.
