"""
preprocessing_pipeline.py

Production-ready preprocessing pipeline.

Responsibilities
----------------
1. Clean text
2. Encode labels
3. Tokenize text
4. Process Hugging Face datasets using dataset.map()
"""

from src.preprocessing.text_cleaner import TextCleaner
from src.preprocessing.label_encoder import LabelEncoder
from src.preprocessing.tokenizer import TextTokenizer


class PreprocessingPipeline:

    def __init__(
        self,
        model_name: str = "bert-base-uncased",
        max_length: int = 128,
    ):

        self.cleaner = TextCleaner()

        self.label_encoder = LabelEncoder()

        self.tokenizer = TextTokenizer(
            model_name=model_name,
            max_length=max_length,
        )

    ####################################################################
    # Detect text column
    ####################################################################

    @staticmethod
    def detect_text_column(sample):

        candidates = [
            "text",
            "comment_text",
            "sentence",
            "review",
            "content",
            "tweet",
            "document",
        ]

        for column in candidates:
            if column in sample:
                return column

        raise ValueError("No text column found.")

    ####################################################################
    # Process one sample
    ####################################################################

    def process_sample(
        self,
        sample,
        num_classes=None,
    ):

        text_column = self.detect_text_column(sample)

        # Clean text
        cleaned_text = self.cleaner.clean(sample[text_column])

        # Encode labels
        encoded = self.label_encoder.encode(
            sample,
            num_classes=num_classes,
        )

        # Tokenize
        tokenized = self.tokenizer.encode(cleaned_text)

        return {

            "text": cleaned_text,

            "input_ids":
                tokenized["input_ids"].squeeze(0).tolist(),

            "attention_mask":
                tokenized["attention_mask"].squeeze(0).tolist(),

            "token_type_ids":
                tokenized["token_type_ids"].squeeze(0).tolist(),

            "labels":
                encoded["labels"],

            "task":
                encoded["task"],
        }

    ####################################################################
    # Internal map function
    ####################################################################

    def _map_function(
        self,
        sample,
        num_classes=None,
    ):

        return self.process_sample(
            sample,
            num_classes=num_classes,
        )

    ####################################################################
    # Process dataset
    ####################################################################

    def process_dataset(
        self,
        dataset,
        num_classes=None,
    ):
        original_columns = dataset.column_names

        processed_dataset = dataset.map(

            lambda sample:
                self._map_function(
                    sample,
                    num_classes=num_classes,
                ),

            remove_columns=original_columns,
            desc="Preprocessing Dataset",

        )

        return processed_dataset