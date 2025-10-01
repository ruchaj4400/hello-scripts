import json
import argparse

def transform_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))  # just pretty-print as a start

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transform a JSON file")
    parser.add_argument("file", help="Path to JSON file")
    args = parser.parse_args()
    transform_json(args.file)