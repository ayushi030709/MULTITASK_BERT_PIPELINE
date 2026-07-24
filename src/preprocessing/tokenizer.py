"""
tokenizer.py

Wrapper around Hugging Face AutoTokenizer.

Features
--------
- Supports any Hugging Face Transformer model
- Single text encoding
- Batch encoding
- Tokenization
- Decoding
- Vocabulary information
- Special tokens
"""

from typing import Dict, List

from transformers import AutoTokenizer

from src.utils.logger import logger


class TextTokenizer:
    """
    Wrapper around Hugging Face AutoTokenizer.

    Example
    -------
    tokenizer = TextTokenizer()

    encoded = tokenizer.encode("I love NLP")

    batch = tokenizer.encode_batch([
        "Hello",
        "How are you?"
    ])
    """

    def __init__(
        self,
        model_name: str = "bert-base-uncased",
        max_length: int = 128,
    ):

        self.model_name = model_name
        self.max_length = max_length

        logger.info(f"Loading tokenizer: {model_name}")

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

        logger.info("Tokenizer loaded successfully.")

    ####################################################################
    # Tokenize
    ####################################################################

    def tokenize(self, text: str) -> List[str]:
        """
        Tokenize text into sub-word tokens.

        Parameters
        ----------
        text : str

        Returns
        -------
        List[str]
        """

        return self.tokenizer.tokenize(text)

    ####################################################################
    # Encode Single Text
    ####################################################################

    def encode(self, text: str) -> Dict:
        """
        Encode a single sentence.

        Returns
        -------
        Dictionary containing:

        - input_ids
        - attention_mask
        - token_type_ids (if supported)
        """

        return self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_attention_mask=True,
            return_token_type_ids=True,
            return_tensors="pt",
        )

    ####################################################################
    # Encode Batch
    ####################################################################

    def encode_batch(
        self,
        texts: List[str],
    ) ->Dict:
        """
        Encode multiple texts.
        """

        return self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_attention_mask=True,
            return_token_type_ids=True,
            return_tensors="pt",
        )

    ####################################################################
    # Decode
    ####################################################################

    def decode(
        self,
        input_ids,
    ) -> str:
        """
        Decode token ids back to text.
        """

        return self.tokenizer.decode(
            input_ids,
            skip_special_tokens=True,
        )

    ####################################################################
    # Vocabulary Size
    ####################################################################

    @property
    def vocab_size(self) -> int:
        """
        Return tokenizer vocabulary size.
        """

        return self.tokenizer.vocab_size

    ####################################################################
    # Special Tokens
    ####################################################################

    @property
    def special_tokens(self):
        """
        Return tokenizer special tokens.
        """

        return self.tokenizer.special_tokens_map

    ####################################################################
    # Hugging Face Tokenizer
    ####################################################################

    def get_tokenizer(self):
        """
        Return underlying Hugging Face tokenizer.
        """

        return self.tokenizer

    ####################################################################
    # Information
    ####################################################################

    def info(self):
        """
        Print tokenizer information.
        """

        logger.info(f"Model Name      : {self.model_name}")
        logger.info(f"Vocabulary Size : {self.vocab_size}")
        logger.info(f"Max Length      : {self.max_length}")