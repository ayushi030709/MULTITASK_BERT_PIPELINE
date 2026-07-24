"""
run_preprocessing.py

Runs preprocessing on all datasets and saves them to disk.

Directory Structure
-------------------
data/
├── raw/
│   ├── go_emotions/
│   ├── tweet_eval/
│   └── toxic_comments/
│
└── processed/
    ├── go_emotions/
    ├── tweet_eval/
    └── toxic_comments/
"""

import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


class DatasetPreprocessor:

    def __init__(self):

        # Import here to avoid Windows DLL initialization issues
        from src.preprocessing.preprocessing_pipeline import (
            PreprocessingPipeline,
        )

        self.pipeline = PreprocessingPipeline()

        self.raw_dir = Path("data/raw")
        self.processed_dir = Path("data/processed")

        self.processed_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

    #############################################################

    @staticmethod
    def is_unlabeled_dataset(dataset):
        """
        Returns True if every label in the first sample is None.
        Useful for Kaggle competition test sets.
        """

        sample = dataset[0]

        binary_columns = [
            "toxic",
            "severe_toxic",
            "obscene",
            "threat",
            "insult",
            "identity_hate",
        ]

        if all(col in sample for col in binary_columns):

            return all(
                sample[col] is None
                for col in binary_columns
            )

        return False

    #############################################################

    def preprocess_split(
        self,
        dataset_name,
        split_name,
        dataset,
        num_classes=None,
    ):

        logger.info(
            f"Processing {dataset_name}/{split_name}"
        )

        if self.is_unlabeled_dataset(dataset):

            logger.warning(
                f"Skipping {dataset_name}/{split_name}"
                " (labels unavailable)"
            )

            return

        processed = self.pipeline.process_dataset(
            dataset,
            num_classes=num_classes,
        )

        save_path = (
            self.processed_dir
            / dataset_name
            / split_name
        )

        save_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        processed.save_to_disk(str(save_path))

        logger.info(f"Saved -> {save_path}")

    #############################################################

    def preprocess_dataset(
        self,
        dataset_name,
        num_classes=None,
    ):

        from datasets import load_from_disk

        dataset_path = self.raw_dir / dataset_name

        logger.info(f"Loading {dataset_path}")

        dataset_dict = load_from_disk(str(dataset_path))

        for split_name, dataset in dataset_dict.items():

            self.preprocess_split(
                dataset_name=dataset_name,
                split_name=split_name,
                dataset=dataset,
                num_classes=num_classes,
            )

    #############################################################

    def run(self):

        datasets = [
            ("go_emotions", 28),
            ("tweet_eval", 3),
            ("toxic_comments", None),
        ]

        for dataset_name, num_classes in datasets:

            logger.info("=" * 60)

            logger.info(
                f"Starting preprocessing for {dataset_name}"
            )

            self.preprocess_dataset(
                dataset_name,
                num_classes,
            )

        logger.info("=" * 60)
        logger.info("Preprocessing completed successfully!")



if __name__ == "__main__":

    DatasetPreprocessor().run()