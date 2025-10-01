import argparse

def count_tokens(file_path):
    with open(file_path, 'r') as f:
        text = f.read()
    tokens = text.split()
    print(f"Total words: {len(tokens)}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument("file", help="Path to text file")
    args = parser.parse_args()
    count_tokens(args.file)