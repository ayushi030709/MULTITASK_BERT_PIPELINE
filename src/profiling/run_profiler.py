"""
run_profiler.py

Entry point for profiling all datasets.

Usage:
------
python -m src.profiling.run_profiler
"""

from pathlib import Path

from datasets import load_from_disk

from .profiler import DatasetProfiler
from .report_generator import ReportGenerator
from .visualizer import DatasetVisualizer


# ============================================================
# DATASET PATHS
# ============================================================

DATASETS = {
    "go_emotions": Path("data/raw/go_emotions"),
    "tweet_eval": Path("data/raw/tweet_eval"),
    "toxic_comments": Path("data/raw/toxic_comments"),
}


# ============================================================
# LOAD DATASET
# ============================================================

def load_dataset(dataset_path: Path):
    """
    Load a HuggingFace dataset saved with load_from_disk().
    """
    return load_from_disk(str(dataset_path))


# ============================================================
# PROFILE SINGLE DATASET
# ============================================================

def profile_dataset(dataset_name: str, dataset_path: Path):

    print("=" * 80)
    print(f"Profiling Dataset : {dataset_name}")
    print("=" * 80)

    if not dataset_path.exists():

        print(f"[ERROR] Dataset not found: {dataset_path}")
        return

    # --------------------------------------------------------

    dataset = load_dataset(dataset_path)

    profiler = DatasetProfiler(
        dataset=dataset,
        dataset_name=dataset_name,
    )

    report = profiler.profile()

    # --------------------------------------------------------

    report_generator = ReportGenerator()

    report_generator.generate(
        dataset_name,
        report,
    )

    # --------------------------------------------------------

    visualizer = DatasetVisualizer()

    visualizer.generate(
        dataset_name,
        profiler.get_all_dataframes(),
    )

    print(f"[SUCCESS] Finished profiling {dataset_name}\n")


# ============================================================
# MAIN
# ============================================================

def main():

    print("\n")
    print("=" * 80)
    print("NLP DATASET PROFILING")
    print("=" * 80)
    print("\n")

    for dataset_name, dataset_path in DATASETS.items():

        try:

            profile_dataset(
                dataset_name,
                dataset_path,
            )

        except Exception as e:

            print(f"[FAILED] {dataset_name}")
            print(e)
            print()

    print("=" * 80)
    print("ALL DATASETS PROCESSED")
    print("=" * 80)


if __name__ == "__main__":
    main()