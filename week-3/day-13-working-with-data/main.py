# Day 13 — Working With Data
# Task: Load a CSV, manipulate lists and dicts, clean data, and print a summary.
# Submit this script along with your original CSV and the output CSV.

import csv
import os

INPUT_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


# ── Step 1: Load CSV ──────────────────────────────────────────────────────────
# Open the CSV file using csv.DictReader and read each row into a list of dicts.

def load_data(filepath):
    rows = []
    # TODO: open the file and read rows into the list
    try:
        with open(filepath, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Please create it first.")
    return rows


# ── Step 2: Print Summary ─────────────────────────────────────────────────────
# Print the total number of rows.
# For any numeric column, print the minimum, maximum, and average values.

def print_summary(rows):
    # TODO: implement summary statistics
    if not rows:
        print("No data available to summarize.")
        return

    print(f"Total number of rows: {len(rows)}\n")
    print("--- Summary Statistics ---")

    # Find which columns are numeric and extract their values
    for key in rows[0].keys():
        numeric_values = []
        is_numeric = True
        
        for row in rows:
            try:
                # Attempt to convert to float to check if numeric
                val = float(row[key])
                numeric_values.append(val)
            except ValueError:
                is_numeric = False
                break
                
        # If the column successfully converted to floats, print stats
        if is_numeric and numeric_values:
            col_min = min(numeric_values)
            col_max = max(numeric_values)
            col_avg = sum(numeric_values) / len(numeric_values)
            
            # Formatting to remove trailing decimals for integers
            print(f"Column '{key}':")
            print(f"  Min: {col_min:g}")
            print(f"  Max: {col_max:g}")
            print(f"  Avg: {col_avg:.2f}\n")
    pass


# ── Step 3: Filter Data ───────────────────────────────────────────────────────
# Return only the rows where a specific column meets a condition.
# Example: score above 70, or price below 50.

def filter_data(rows):
    filtered = []
    # TODO: define and apply your filter condition
    # Filter condition: 'score' must be greater than 70
    for row in rows:
        if float(row['score']) > 70:
            filtered.append(row)
    return filtered


# ── Step 4: Sort and Export ───────────────────────────────────────────────────
# Sort the filtered data by one column and write the result to OUTPUT_FILE.

def save_data(rows, filepath):
    # TODO: sort rows by a column, then write to CSV
    if not rows:
        print("No data to save.")
        return

    # Sort rows descending by 'score'
    sorted_rows = sorted(rows, key=lambda x: float(x['score']), reverse=True)

    # Ensure the directory exists before saving
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, mode='w', encoding='utf-8', newline='') as f:
        fieldnames = sorted_rows[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(sorted_rows)
    pass


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    rows = load_data(INPUT_FILE)
    print_summary(rows)
    filtered = filter_data(rows)
    save_data(filtered, OUTPUT_FILE)
    print(f"Done. {len(filtered)} rows written to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
