# denguedatasets

[![PyPI version](https://img.shields.io/pypi/v/denguedatasets.svg)](https://pypi.org/project/denguedatasets-py/)
[![Downloads](https://img.shields.io/pypi/dm/denguedatasets.svg)](https://pypi.org/project/denguedatasets-py/)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)


The `denguedasets` package provide a curated collection of open-access dengue fever surveillance and climate
datasets for epidemiological research and machine learning. Includes surveillance records, climatic co-variates, 
and mortality indicators from Bangladesh, the Philippines, Taiwan, Sri Lanka, Brazil, Colombia, 
Pakistan, India, Peru, Indonesia, and Sierra Leone, spanning case counts, 
deaths, case-fatality rates, and associated meteorological variables 
(temperature, humidity, precipitation) suitable for spatiotemporal analysis, 
outbreak prediction, machine learning, and time-series modeling from Kaggle."

## Installation

You can install the `denguedatasets` package from PyPI
```bash
pip install denguedatasets
```

## Usage
```bash
import denguedatasets as dd
```


## Quick start

```python
import denguedatasets as dd

# List all available datasets
dd.list_datasets()

# Inspect metadata (source, license, description) before loading
dd.dataset_info("dengue_taiwan")

# Load a dataset as a pandas DataFrame
df = dd.load_dataset("dengue_taiwan")
df.head()

# Describe dataset
df = dd.describe("dengue_taiwan")
print(df)

```

`load_dataset` accepts any keyword argument supported by
`pandas.read_csv`, forwarded directly:

```python
df = dd.load_dataset("dengue_brazil", sep=";", encoding="latin-1")
```

## Some available datasets

| Key                           | Country / Region              | Period    | License            |
| ----------------------------- | ----------------------------- | --------- | ------------------ |
| `dengue_bangladesh`           | Bangladesh (Dhaka)            | —         | CC BY 4.0          |
| `dengue_bangladesh_mortality` | Bangladesh                    | 2000–2024 | MIT                |
| `dengue_brazil`               | Brazil                        | 2000–2019 | GPL 2              |
| `dengue_brazil_labels`        | Brazil (data dictionary)      | 2000–2019 | GPL 2              |
| `dengue_colombia`             | Colombia (all municipalities) | 2007–2019 | Unknown            |
| `dengue_colombia_medellin`    | Colombia (Medellín)           | 2007–2019 | Unknown            |
| `dengue_india`                | India                         | —         | CC0                |
| `dengue_jakarta`              | Indonesia (Jakarta)           | 2021–2024 | Unknown            |
| `dengue_pakistan`             | Pakistan                      | 2016–2020 | CC BY-SA 4.0       |
| `dengue_peru`                 | Peru                          | 2019–2022 | Apache 2.0         |
| `dengue_philippines`          | Philippines                   | 2016–2020 | CC0                |
| `dengue_sierra_leone`         | Sierra Leone (Freetown)       | 2015–2024 | CC BY-SA 4.0       |
| `dengue_sri_lanka`            | Sri Lanka                     | 2010–2020 | © Original Authors |
| `dengue_sri_lanka_2019`       | Sri Lanka                     | 2019      | CC0                |
| `dengue_sri_lanka_2020`       | Sri Lanka                     | 2020      | CC0                |
| `dengue_sri_lanka_2021`       | Sri Lanka                     | 2021      | CC0                |
| `dengue_taiwan`               | Taiwan                        | 1998–2024 | CC0                |

Full details for each dataset (original source URL, license text, original
filename, and description) are documented in [`datasets.md`](datasets.md).

> Run `denguedasets.list_datasets` or `dd.list_datasets` (using `dd` as alias) to see the full list of availabale datasets.

## Disclaimer

The datasets included in `denguedasets` are provided strictly for educational,
research, and informational purposes. Every dataset bundled with this package originates from a public Kaggle
dataset. Each retains its **original license** as declared by its
publisher (see the table above and `datasets.md`); this package does not
relicense the underlying data. Users redistributing or publishing
derived work should check the individual dataset license before reuse.

The author of `denguedasets` makes no warranties, express or implied, regarding the accuracy,
completness, or suitability of any datasets for a particular purpose. Users are solely responsible for ensuring that
their use of these datasets complies with applicable laws, regulations, and ethical guidelines.

Anu finding, conclusions, or decisions derived from the use of these datasets are the soloe responsibility of the user.
The author shall not be held liable for any direct, indirect, or consequential damages arising from the use or
misuse of the datasets included in this package.


## Development

```bash
git clone https://github.com/fdzul/denguedatasets-py.git
cd denguedatasets_py
pip install -e ".[dev]"
pytest -v
```

## Citation

If you use this package in your research, please cite it as:

> Dzul Manzanilla, F.A. & Correa Morales, F. (2026). *denguedatasets*:
> A curated collection of open-access dengue fever datasets for
> epidemiological research (Version 0.1.0) [Software].
> https://github.com/fdzul/denguedatasets-py

## Authors

- **Felipe A. Dzul Manzanilla** — [ORCID: 0000-0002-2085-9141](https://orcid.org/0000-0002-2085-9141) — Instituto Nacional de Salud Pública (INSP), Mexico
- **Fabián Correa Morales** — [ORCID: 0000-0002-6193-1242](https://orcid.org/0000-0002-6193-1242) — Centro Nacional de Programas Preventivos y Control de Enfermedades (CENAPRECE), Mexico

## License

The `denguedatasets` library es release under **GNU General Public License v3.0 (GPL-3.0)**, which ensures that all source code
and derived works remain free and open-source. See [LICENSE](LICENSE) for details. Individual datasets retain their own
original licenses as documented in `datasets.md`.
