import argparse
import re

def count_tokens(file_path):
    with open(file_path, 'r', encoding="utf-8") as f:
        text = f.read()
        
    tokens = text.findall(r"\w+", text)
    print("Text Token Counter")
    print("------------------")
    print(f"Number of tokens (words): {len(tokens)}")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count words in a text file")
    parser.add_argument("file", help="Path to text file")
    args = parser.parse_args()
    count_tokens(args.file)