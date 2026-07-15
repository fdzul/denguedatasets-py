# Getting Started

This guide will help you install denguedatasets and load your first dengue dataset in a few minutes.

## Prerequisites

Python 3.8 or higher.
pandas (installed automatically with denguedatasets).
Installation

From PyPI (Recommended)

The easiest way to install the package is directly from the Python Package Index:

```bash
pip install denguedatasets

```

From GitHub

If you want the latest development version, you can install it directly from the repository:

```bash
pip install git+https://github.com/fdzul/denguedatasets-py
```

## 1. Your First Dataset

Once installed, using the package is straightforward. Follow these three steps:

1. Import the package

```python
import denguedatasets as dd
```
## 2. See what is available

List all datasets included in the package to find the key you need:

```python
print(dd.list_datasets())
```

## 3. Load and analyze

Load the dataset into a pandas DataFrame and start working:

```python
# Load Taiwan dengue data
df = dd.load_dataset("dengue_taiwan")

# Display the first 5 rows
print(df.head())

# Check the shape of the data
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
```


