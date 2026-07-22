from datasets import load_dataset


def download_dataset(dataset_path, config=None, dataset_type="hf"):
    """
    Downloads a dataset from Hugging Face.

    dataset_type:
        - hf  : Standard Hugging Face dataset
        - csv : CSV files hosted on Hugging Face
    """

    if dataset_type == "hf":

        if config:
            return load_dataset(dataset_path, config)

        return load_dataset(dataset_path)

    elif dataset_type == "csv":

        return load_dataset(
            dataset_path,
            data_files={
                "train": "train.csv.gz",
                "test": [
                    "test.csv.gz",
                    "test_labels.csv.gz"
                ]
            }
        )

    else:
        raise ValueError(f"Unknown dataset type: {dataset_type}")