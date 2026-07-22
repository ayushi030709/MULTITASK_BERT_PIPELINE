from pathlib import Path

from datasets import load_dataset


DATA_DIR = Path("data/raw")


def download_go_emotions():
    print("Downloading GoEmotions...")

    dataset = load_dataset(
        "google-research-datasets/go_emotions",
        "simplified"
    )

    save_path = DATA_DIR / "go_emotions"

    dataset.save_to_disk(save_path)

    print(f"Saved GoEmotions to {save_path}")


if __name__ == "__main__":
    download_go_emotions()