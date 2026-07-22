"""
visualizer.py

Visualization module for dataset profiling.

Creates:
- Text length histogram
- Label distribution chart
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from .statistic import Statistics


class DatasetVisualizer:

    def __init__(self, output_dir="reports"):

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    ####################################################################
    # DIRECTORY
    ####################################################################

    def _plot_directory(self, dataset_name):

        plot_dir = self.output_dir / dataset_name / "plots"
        plot_dir.mkdir(parents=True, exist_ok=True)

        return plot_dir

    ####################################################################
    # TEXT LENGTH
    ####################################################################

    def plot_text_length(
        self,
        dataset_name,
        dataframe,
        split_name,
    ):

        text_column = Statistics.detect_text_column(dataframe)

        lengths = dataframe[text_column].astype(str).str.len()

        plt.figure(figsize=(10, 6))

        plt.hist(
            lengths,
            bins=40,
            edgecolor="black"
        )

        plt.title(f"{dataset_name} ({split_name}) Text Length Distribution")
        plt.xlabel("Characters")
        plt.ylabel("Frequency")

        plt.tight_layout()

        save_path = (
            self._plot_directory(dataset_name)
            / f"{split_name}_text_length.png"
        )

        plt.savefig(save_path, dpi=300)
        plt.close()

    ####################################################################
    # LABEL DISTRIBUTION
    ####################################################################

    def plot_label_distribution(
        self,
        dataset_name,
        dataframe,
        split_name,
    ):

        distribution = Statistics.label_distribution(dataframe)

        if len(distribution) == 0:
            return

        labels = list(distribution.keys())
        values = list(distribution.values())

        plt.figure(figsize=(12, 6))

        plt.bar(
            range(len(labels)),
            values
        )

        plt.xticks(
            range(len(labels)),
            labels,
            rotation=45,
            ha="right"
        )

        plt.title(f"{dataset_name} ({split_name}) Label Distribution")
        plt.xlabel("Labels")
        plt.ylabel("Count")

        plt.tight_layout()

        save_path = (
            self._plot_directory(dataset_name)
            / f"{split_name}_label_distribution.png"
        )

        plt.savefig(save_path, dpi=300)
        plt.close()

    ####################################################################
    # GENERATE
    ####################################################################

    def generate(
        self,
        dataset_name,
        dataframes,
    ):

        print(f"[INFO] Creating plots for {dataset_name}")

        for split_name, dataframe in dataframes.items():

            self.plot_text_length(
                dataset_name,
                dataframe,
                split_name,
            )

            self.plot_label_distribution(
                dataset_name,
                dataframe,
                split_name,
            )

        print(f"[SUCCESS] Finished plots for {dataset_name}")