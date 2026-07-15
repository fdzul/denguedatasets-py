# denguedatasets documentation


## Welcome

The **denguedasets** package provide a curated collection of open-access dengue fever surveillance and climate datasets for epidemiological research and machine learning. Includes surveillance records, climatic co-variates, and mortality indicators from Bangladesh, the Philippines, Taiwan, Sri Lanka, Brazil, Colombia, Pakistan, India, Peru, Indonesia, and Sierra Leone, spanning case counts, deaths, case-fatality rates, and associated meteorological variables (temperature, humidity, precipitation) suitable for spatiotemporal analysis, outbreak prediction, machine learning, and time-series modeling from Kaggle.

## Philosophy

The authors' vision is to create data packages, functions, or a combination of both in **Julia**, **R**, and **Python**, contributing to the interoperability of algorithms and data to transform the information into decisions that help solve specific problems.

In the case of data packages, the authors' vision is to create specialized packages focused on specific topics and subtopics. Instead of searching through multiple diverse and heterogeneous sources, users can access all these interesting datasets in a single package.

Specifically, in the case of the **denguedasets** package, each included dataset is specialized in dengue fever, providing a valuable source of information for academics, data scientists, statisticians, modelers, university professors, or students interested in working with this combination of topics.


## Getting Started

### Installation

#### From  PyPI

The easiest way to install the **denguedatasets** package is directlty from PyPI:

```bash
pip install denguedatasets
```

#### From GitHub

To get the latest development version with newest features and bugs fixes is directlty from GitHub:

```bash
pip install git+https://github.com/fdzul/denguedatasets-py
```

### Quick Start Tutorial


#### 1. Import the package
```python
import denguedatasets as dd
```

#### 2. List available datasets

See all dataset included in the **denguedatasets** package:

```python
datasets = dd.list_datasets()
print(datasets)
```

#### 3. Load a Datasets

Load any dataset as pandas DataFrame:

```python

# 3.1. Load dengue dataset from Brazil
df = dd.load_dataset("dengue_brazil")

# 3.2. Display the first rows
print(df.head())

# 3.3 Check dataset dimensions

print(f"Shape: {df.shape}")
```

#### 4. Describe a datasets

```python
df = dd.describe("dengue_taiwan")
print(df)
```
