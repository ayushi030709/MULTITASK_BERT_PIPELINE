from pathlib import Path

from src.data_ingestion.config import DATASETS, RAW_DATA_DIR
from src.data_ingestion.dataset_loader import download_dataset
from src.data_ingestion.validate import validate_dataset


def save_dataset(dataset, output_path: Path):
    """
    Save the dataset to disk.
    """
    dataset.save_to_disk(output_path)


def main():

    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    for dataset_name, dataset_info in DATASETS.items():

        print(f"\nDownloading {dataset_name}...")

        dataset = download_dataset(
         dataset_path=dataset_info["path"],
         config=dataset_info.get("config"),
         dataset_type=dataset_info.get("type", "hf")
)

        validate_dataset(dataset)

        output_path = RAW_DATA_DIR / dataset_name

        save_dataset(dataset, output_path)

        print(f"Saved {dataset_name} to {output_path}")


if __name__ == "__main__":
    main()