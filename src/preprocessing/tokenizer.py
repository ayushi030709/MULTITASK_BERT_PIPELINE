from transformers import AutoTokenizer
from src.utils.logger import logger


class BertTokenizerWrapper:
    """
    Wrapper around Hugging Face BERT tokenizer.
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

    def tokenize(self, text: str):
        """
        Return tokenized words.
        """
        return self.tokenizer.tokenize(text)

    def encode(self, text: str):
        """
        Encode a single sentence.
        """
        return self.tokenizer(
            text,
            padding="max_length",
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

    def encode_batch(self, texts):
        """
        Encode multiple sentences.
        """
        return self.tokenizer(
            texts,
            padding=True,
            truncation=True,
            max_length=self.max_length,
            return_tensors="pt",
        )

    def decode(self, ids):
        """
        Convert ids back to text.
        """
        return self.tokenizer.decode(
            ids,
            skip_special_tokens=True,
        )

    def vocab_size(self):
        """
        Return vocabulary size.
        """
        return self.tokenizer.vocab_size

    def special_tokens(self):
        """
        Return special token dictionary.
        """
        return self.tokenizer.special_tokens_map

    def get_tokenizer(self):
        """
        Return raw Hugging Face tokenizer.
        """
        return self.tokenizer