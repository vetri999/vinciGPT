# process/train.py
from pathlib import Path
from datasets import load_dataset

# Input:   TinyStories dataset from Hugging Face Hub (via `datasets`)
# Process: Download + cache, then persist locally as Arrow shards (`save_to_disk`)
# Output:  input/raw_data/tinystories/  (HF dataset directory)
# Where this output is used: Next units will load_from_disk() → tokenize → write train.bin/val.bin

DATASET_ID = "roneneldan/TinyStories"
RAW_DIR = Path(__file__).resolve().parents[1] / "input" / "raw_data" / "tinystories"

def main():
    RAW_DIR.parent.mkdir(parents=True, exist_ok=True)
    if RAW_DIR.exists():
        print(f"[ok] raw data already present: {RAW_DIR}")
        return
    ds = load_dataset(DATASET_ID)       # downloads + caches
    ds.save_to_disk(str(RAW_DIR))       # writes Arrow shards
    print(f"[ok] saved raw data: {RAW_DIR}")

if __name__ == "__main__":
    main()
