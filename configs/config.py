from pathlib import Path
import torch

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

AUGMENTED_DATA_DIR = DATA_DIR / "augmented"

MODEL_DIR = PROJECT_ROOT / "saved_models"

LOG_DIR = PROJECT_ROOT / "logs"

EXPERIMENT_DIR = PROJECT_ROOT / "experiments"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

RANDOM_SEED = 42

MAX_LENGTH = 256

BATCH_SIZE = 16

LEARNING_RATE = 2e-5

NUM_EPOCHS = 3

MODEL_NAME = "bert-base-uncased"