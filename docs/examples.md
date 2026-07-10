# denguedatasets – Examples

This page provides practical examples of using `denguedatasets` for data analysis and exploration.

## Basic Examples

### Example 1: Loading and Exploring a Dataset

Learn how to load a dataset and perform basic exploration.

```python
import denguedatasets as dd

# Load the dengue cases of colombia.
den_col = dd.load_dataset("dengue_colombia")

# Display first few rows
print(den_col.head())

# Check dataset shape
print(f"\nDataset shape: {den_col.shape}")

# View column names
print(f"\nColumns: {list(den_col.columns)}")

# Get summary statistics
print("\nSummary statistics:")
print(den_col.describe())

# Check for missing values
print("\nMissing values:")
print(den_col.isnull().sum())

```

### Example 2: Exploring dengue cases in Brazil.

```python

import denguedatasets as dd

den_brazil = dd.load_dataset("dengue_brazil")
print(den_brazil.head())
print(f"\nDataset shape: {den_brazil.shape}")
print(f"\nColumns: {list(den_brazil.columns)}")

```

### Example 3: Listing all available datasets

```python

import denguedatasets as dd

datasets = ld.list_datasets()
print(datasets)

```

