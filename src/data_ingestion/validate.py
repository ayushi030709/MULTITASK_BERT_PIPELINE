def validate_dataset(dataset):

    if dataset is None:
        raise ValueError("Dataset download failed.")

    if len(dataset) == 0:
        raise ValueError("Dataset is empty.")

    print("Dataset validation passed.")