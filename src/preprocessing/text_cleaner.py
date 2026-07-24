"""
text_cleaner.py

Text preprocessing utilities for NLP datasets.

Responsibilities
----------------
- Remove URLs
- Remove HTML tags
- Normalize Unicode
- Remove extra whitespaces
- Normalize repeated punctuation
- Optional lowercase conversion
- Optional emoji removal

This module does NOT:
- Tokenize text
- Encode labels
- Save datasets
"""

import html
import re
import unicodedata
from typing import Optional

try:
    import emoji
    EMOJI_AVAILABLE = True
except ImportError:
    EMOJI_AVAILABLE = False


class TextCleaner:
    """
    Production-ready configurable text cleaner.
    """

    URL_PATTERN = re.compile(r"https?://\S+|www\.\S+")
    HTML_PATTERN = re.compile(r"<.*?>")
    MULTISPACE_PATTERN = re.compile(r"\s+")
    REPEATED_PUNCT_PATTERN = re.compile(r"([!?.,])\1+")

    def __init__(
        self,
        lowercase: bool = True,
        remove_urls: bool = True,
        remove_html: bool = True,
        remove_emojis: bool = False,
        normalize_unicode: bool = True,
        normalize_whitespace: bool = True,
        normalize_punctuation: bool = True,
    ):

        self.lowercase = lowercase
        self.remove_urls = remove_urls
        self.remove_html = remove_html
        self.remove_emojis = remove_emojis
        self.normalize_unicode = normalize_unicode
        self.normalize_whitespace = normalize_whitespace
        self.normalize_punctuation = normalize_punctuation

    ############################################################

    def _remove_urls(self, text: str) -> str:
        return self.URL_PATTERN.sub("", text)

    ############################################################

    def _remove_html(self, text: str) -> str:
        text = html.unescape(text)
        return self.HTML_PATTERN.sub("", text)

    ############################################################

    def _normalize_unicode(self, text: str) -> str:
        return unicodedata.normalize("NFKC", text)

    ############################################################

    def _remove_emojis(self, text: str) -> str:

        if not EMOJI_AVAILABLE:
            return text

        return emoji.replace_emoji(text, replace="")

    ############################################################

    def _normalize_punctuation(self, text: str) -> str:
        """
        !!!!! -> !
        ???? -> ?
        """
        return self.REPEATED_PUNCT_PATTERN.sub(r"\1", text)

    ############################################################

    def _normalize_whitespace(self, text: str) -> str:
        return self.MULTISPACE_PATTERN.sub(" ", text).strip()

    ############################################################

    def clean(self, text: Optional[str]) -> str:

        if text is None:
            return ""

        text = str(text)

        if self.normalize_unicode:
            text = self._normalize_unicode(text)

        if self.remove_html:
            text = self._remove_html(text)

        if self.remove_urls:
            text = self._remove_urls(text)

        if self.remove_emojis:
            text = self._remove_emojis(text)

        if self.normalize_punctuation:
            text = self._normalize_punctuation(text)

        if self.normalize_whitespace:
            text = self._normalize_whitespace(text)

        if self.lowercase:
            text = text.lower()

        return text

    ############################################################

    def clean_batch(self, texts):

        return [self.clean(text) for text in texts]