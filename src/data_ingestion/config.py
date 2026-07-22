from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

DATASETS = {
    "go_emotions": {
        "path": "google-research-datasets/go_emotions",
        "config": "simplified",
        "type": "hf"
    },

    "tweet_eval": {
        "path": "tweet_eval",
        "config": "sentiment",
        "type": "hf"
    },

    "toxic_comments": {
        "path": "Heliosoph/Jigsaw-Toxic-Comments",
        "type": "csv"
    }
}