from src.preprocessing.preprocessing_pipeline import PreprocessingPipeline

from datasets import Dataset

dataset = Dataset.from_list(
    [
        {
            "text": "I LOVE this movie!!!!! 😍😍",
            "label": 2,
        },
        {
            "text": "This movie is terrible!!!",
            "label": 0,
        },
    ]
)

pipeline = PreprocessingPipeline()

processed = pipeline.process_dataset(dataset)

print(processed)
print()
print(processed[0])