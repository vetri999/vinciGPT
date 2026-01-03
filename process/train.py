"""
Step 1 : Get training data

Input = TinyStories dataset in HuggingFace datasets library

Process:
1. Create a folder
2. Download data
3. Save data in Arrow shards format to the folder

Output = TinyStories dataset in your Projects folder

Where is this Output used?
1. Tokenization
2. Splitting dataset into train and validation bins
"""


from pathlib import Path
from datasets import load_dataset

RAW_DIR = Path(__file__).resolve().parents[1] / "input" / "raw_data" / "tinystories"

def main():
    RAW_DIR.parent.mkdir(parents=True, exist_ok=True)             # 1. Create a folder. Plus a check to alert if data is already present
    if RAW_DIR.exists(): 
        print(f"[ok] raw data already present: {RAW_DIR}") 
        return
    ds = load_dataset("roneneldan/TinyStories")                   # 2. Download data
    ds.save_to_disk(str(RAW_DIR))                                 # 3. Save data in Arrow shards format to the folder
    print(f"[ok] saved raw data: {RAW_DIR}")

if __name__ == "__main__":
    main()