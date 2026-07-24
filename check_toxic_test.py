from datasets import load_from_disk

dataset = load_from_disk("data/raw/toxic_comments")

print("Splits:", dataset)

print("\nColumns:")
print(dataset["test"].column_names)

print("\nFirst sample:")
print(dataset["test"][0])