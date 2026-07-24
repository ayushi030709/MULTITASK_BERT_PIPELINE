"""
label_encoder.py

Encodes labels for different NLP tasks.

Supported Tasks
---------------
1. Single-label classification
2. Multi-label classification
3. Multi-binary classification
"""

from typing import List, Dict, Any

import numpy as np


class LabelEncoder:

    def __init__(self):

        # Toxic Comment label columns
        self.toxic_columns = [
            "toxic",
            "severe_toxic",
            "obscene",
            "threat",
            "insult",
            "identity_hate",
        ]

    ####################################################################
    # Detect dataset type
    ####################################################################

    def detect_task_type(self, sample: Dict[str, Any]) -> str:

        # GoEmotions
        if "labels" in sample:
            return "multi_label"

        # TweetEval
        if "label" in sample:
            return "single_label"

        # Toxic Comments
        if all(col in sample for col in self.toxic_columns):
            return "multi_binary"

        raise ValueError("Unsupported dataset format.")

    ####################################################################
    # Single Label
    ####################################################################

    def encode_single_label(
        self,
        label: int,
    ) -> int:

        return int(label)

    ####################################################################
    # Multi Label
    ####################################################################

    def encode_multi_label(
        self,
        labels: List[int],
        num_classes: int,
    ) -> List[int]:

        encoded = np.zeros(num_classes, dtype=np.float32)

        for label in labels:
            encoded[int(label)] = 1.0

        return encoded.tolist()

    ####################################################################
    # Multi Binary
    ####################################################################

    def encode_multi_binary(
        self,
        sample: Dict[str, Any],
    ) -> List[int]:

        return [

            int(sample[column])

            for column in self.toxic_columns

        ]

    ####################################################################
    # Main Encoder
    ####################################################################

    def encode(
        self,
        sample: Dict[str, Any],
        num_classes: int | None = None,
    ):

        task = self.detect_task_type(sample)

        ############################################################

        if task == "single_label":

            return {

                "task": task,

                "labels": self.encode_single_label(
                    sample["label"]
                )

            }

        ############################################################

        if task == "multi_label":

            if num_classes is None:

                raise ValueError(
                    "num_classes is required "
                    "for multi-label datasets."
                )

            return {

                "task": task,

                "labels": self.encode_multi_label(
                    sample["labels"],
                    num_classes,
                )

            }

        ############################################################

        if task == "multi_binary":

            return {

                "task": task,

                "labels": self.encode_multi_binary(
                    sample
                )

            }

        ############################################################

        raise ValueError("Unknown task type.")