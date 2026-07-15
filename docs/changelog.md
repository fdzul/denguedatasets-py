
---
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [0.1.0] - 2026-07-10

### Added

- Initial release of **denguedatasets**.
- 17 curated dengue surveillance and climate datasets from 11 countries: Bangladesh, Brazil, Colombia, India, Indonesia, Pakistan, Peru, Philippines, Sierra Leone, Sri Lanka, and Taiwan.
- `list_datasets()` to list all available dataset keys.
- `dataset_info()` to inspect metadata (source, license, description) before loading.
- `load_dataset()` to load any dataset as a pandas DataFrame, with support for all `pandas.read_csv` keyword arguments.
- `describe()` to generate summary statistics for any dataset.
- Structured metadata for each dataset documented in the Datasets Catalog.
