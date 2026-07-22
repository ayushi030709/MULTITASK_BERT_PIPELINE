"""
profiler.py

Main dataset profiler.

Responsibilities
----------------
1. Convert HuggingFace Dataset -> Pandas once.
2. Call Statistics utility methods.
3. Return one structured report.
"""

from typing import Dict

import pandas as pd
from datasets import DatasetDict

from .statistic import Statistics


class DatasetProfiler:

    def __init__(
        self,
        dataset: DatasetDict,
        dataset_name: str
    ):

        self.dataset_name = dataset_name
        self.dataset = dataset

        # Convert every split only once
        self.dataframes: Dict[str, pd.DataFrame] = {

            split_name: split.to_pandas()

            for split_name, split in dataset.items()

        }

    ####################################################################
    # DATASET INFORMATION
    ####################################################################

    def dataset_information(self):

        information = {}

        for split_name, split in self.dataset.items():

            information[split_name] = {

                "rows": len(split),

                "columns": split.column_names,

                "num_columns": len(split.column_names),

                "features": {

                    name: str(feature)

                    for name, feature in split.features.items()

                }

            }

        return information

    ####################################################################
    # SPLIT SUMMARY
    ####################################################################

    def split_summary(self):

        summary = {}

        for split_name, dataframe in self.dataframes.items():

            summary[split_name] = Statistics.summarize(dataframe)

        return summary

    ####################################################################
    # BUILD REPORT
    ####################################################################

    def profile(self):

        split_statistics = self.split_summary()

        report = {

            "dataset_name": self.dataset_name,

            "dataset_information": self.dataset_information(),

            "missing_values": {

                split: stats["missing_values"]

                for split, stats in split_statistics.items()

            },

            "duplicates": {

                split: stats["duplicates"]

                for split, stats in split_statistics.items()

            },

            "text_statistics": {

                split: stats["text_statistics"]

                for split, stats in split_statistics.items()

            },

            "label_distribution": {

                split: stats["label_distribution"]

                for split, stats in split_statistics.items()

            },

            "random_examples": {

                split: stats["random_examples"]

                for split, stats in split_statistics.items()

            }

        }

        return report

    ####################################################################
    # DATAFRAME ACCESS
    ####################################################################

    def get_dataframe(self, split_name):

        return self.dataframes[split_name]

    def get_all_dataframes(self):

        return self.dataframes