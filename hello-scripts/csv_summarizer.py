import csv
import argparse

def summarize_csv(file_path):
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        
        #print(f"Rows: {len(rows)}")
        if not rows:
            print("The file is empty")
            return
        header = rows[0]
        num_rows = len(rows) -1
        num_cols = len(header)
        
        print("CSV Summary")
        print("-----------")
        print(f"Columns: {', '.join(header)}")
        print(f"Number of rows (excluding header): {num_rows}")
        print(f"Number of columns: {num_cols}")

            
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize a CSV file")
    parser.add_argument("file", help ="Path to CSV file")
    args = parser.parse_args()
    summarize_csv(args.file)