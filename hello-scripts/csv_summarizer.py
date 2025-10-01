import csv
import argparse

def summarize_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        rows = list(reader)
        print(f"Rows: {len(rows)}")
        if rows:
            print(f"Columns: {len(rows[0])}")
            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a CSV file")
    parser.add_argument("file", help ="Path to CSV file")
    args = parser.parse_args()
    summarize_csv(args.file)