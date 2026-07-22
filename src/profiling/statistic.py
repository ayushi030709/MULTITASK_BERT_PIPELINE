"""
statistics.py

Reusable statistical utilities for NLP datasets.

Supports
---------
- Single-label datasets
- Multi-label datasets
- Multi-binary datasets
"""

from collections import Counter
from typing import Dict, List

import numpy as np
import pandas as pd


class Statistics:

    ####################################################################
    # TEXT COLUMN DETECTION
    ####################################################################

    TEXT_COLUMNS = [

        "text",
        "comment_text",
        "sentence",
        "review",
        "content",
        "tweet",
        "document"

    ]

    @classmethod
    def detect_text_column(cls, df: pd.DataFrame) -> str:

        for column in cls.TEXT_COLUMNS:

            if column in df.columns:

                return column

        for column in df.columns:

            if pd.api.types.is_string_dtype(df[column]):

                return column

        raise ValueError("No text column found.")

    ####################################################################
    # LABEL DETECTION
    ####################################################################

    @staticmethod
    def detect_problem_type(df: pd.DataFrame):

        if "label" in df.columns:

            return "single"

        if "labels" in df.columns:

            return "multi"

        binary_columns = []

        for column in df.columns:

            if column in ["id", "text", "comment_text"]:

                continue

            unique = set(df[column].dropna().unique())

            if unique.issubset({0, 1}):

                binary_columns.append(column)

        if len(binary_columns) > 0:

            return "binary"

        return "unknown"

    ####################################################################
    # MISSING VALUES
    ####################################################################

    @staticmethod
    def missing_values(df):

        return df.isnull().sum().to_dict()

    ####################################################################
    # DUPLICATES
    ####################################################################

    @staticmethod
    def duplicates(df):

        temp = df.copy()

        for col in temp.columns:

            temp[col] = temp[col].apply(

                lambda x:

                tuple(x.tolist())

                if isinstance(x, np.ndarray)

                else tuple(x)

                if isinstance(x, list)

                else x

            )

        return int(temp.duplicated().sum())

    ####################################################################
    # TEXT STATS
    ####################################################################

    @classmethod
    def text_statistics(cls, df):

        text_column = cls.detect_text_column(df)

        text = df[text_column].astype(str)

        chars = text.str.len()

        words = text.str.split().str.len()

        return {

            "text_column": text_column,

            "samples": len(df),

            "avg_characters": round(chars.mean(), 2),

            "median_characters": float(chars.median()),

            "min_characters": int(chars.min()),

            "max_characters": int(chars.max()),

            "95_percentile": float(chars.quantile(.95)),

            "99_percentile": float(chars.quantile(.99)),

            "avg_words": round(words.mean(), 2),

            "min_words": int(words.min()),

            "max_words": int(words.max())

        }

    ####################################################################
    # LABEL DISTRIBUTION
    ####################################################################

    @classmethod
    def label_distribution(cls, df):

        task = cls.detect_problem_type(df)

        ##############################################################

        if task == "single":

            return (

                df["label"]

                .value_counts()

                .sort_index()

                .to_dict()

            )

        ##############################################################

        if task == "multi":

            counter = Counter()

            for labels in df["labels"]:

                if isinstance(labels, np.ndarray):

                    labels = labels.tolist()

                counter.update(labels)

            return dict(counter)

        ##############################################################

        if task == "binary":

            distribution = {}

            for column in df.columns:

                if column in [

                    "id",

                    "text",

                    "comment_text"

                ]:

                    continue

                unique = set(df[column].dropna().unique())

                if unique.issubset({0, 1}):

                    distribution[column] = int(df[column].sum())

            return distribution

        ##############################################################

        return {}

    ####################################################################
    # RANDOM EXAMPLES
    ####################################################################

    @staticmethod
    def random_examples(df, n=5):

        return (

            df.sample(

                min(n, len(df)),

                random_state=42

            )

            .to_dict(

                orient="records"

            )

        )

    ####################################################################
    # COMPLETE SUMMARY
    ####################################################################

    @classmethod
    def summarize(cls, df):

        return {

            "missing_values": cls.missing_values(df),

            "duplicates": cls.duplicates(df),

            "text_statistics": cls.text_statistics(df),

            "label_distribution": cls.label_distribution(df),

            "random_examples": cls.random_examples(df)

        }