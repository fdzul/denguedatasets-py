"""
denguedatasets
A Python package providing curated collection of open-access dengue fever surveillance and climate datasets for epidemiological research and machine learning in csv and parquet format from curated of Kaggle and OpenDengue.
"""

__version__ = "0.1.0"

from .core import load_dataset, list_dataset, describe
from .datasets import DATASETS

__all__ = [
     "load_dataset",
     "list_dataset",
     "describe",
     "DATASETS",
     "__version__",
]
