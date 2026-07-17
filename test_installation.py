import torch
import transformers
import datasets
import pandas
import sklearn

print("=" * 60)

print("Environment Successfully Installed")

print("=" * 60)

print("PyTorch:", torch.__version__)

print("Transformers:", transformers.__version__)

print("Datasets:", datasets.__version__)

print("Pandas:", pandas.__version__)

print("Scikit-Learn:", sklearn.__version__)

print("=" * 60)

print("CUDA Available:", torch.cuda.is_available())

if torch.cuda.is_available():

    print("GPU:", torch.cuda.get_device_name(0))

else:

    print("Running on CPU")

print("=" * 60)