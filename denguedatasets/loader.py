"""
Loader utilities for denguedatasets.

Provides the public functions used to discover and load the CSV datasets
bundled with the package:

    - list_datasets()
    - dataset_info(name)
    - load_dataset(name)

Design notes
------------
Files are read via ``importlib.resources`` (not bare file paths) so that
loading works correctly regardless of how the package was installed
(regular install, editable install, wheel, or zipped egg).
"""

from __future__ import annotations

import importlib.resources as pkg_resources
from typing import Any

import pandas as pd

from .datasets import DATASETS

_DATA_PACKAGE = "denguedatasets.data"


class DatasetNotFoundError(KeyError):
    """Raised when a requested dataset name is not in the registry."""


def list_datasets() -> list[str]:
    """Return the sorted list of available dataset names.

    Returns
    -------
    list[str]
        Dataset keys that can be passed to :func:`load_dataset` or
        :func:`dataset_info`.

    Examples
    --------
    >>> import denguedatasets as dd
    >>> "dengue_taiwan" in dd.list_datasets()
    True
    """
    return sorted(DATASETS.keys())


def dataset_info(name: str) -> dict[str, Any]:
    """Return the registry metadata for a single dataset.

    Parameters
    ----------
    name : str
        Dataset key, e.g. ``"dengue_taiwan"``. See :func:`list_datasets`
        for the full list of valid names.

    Returns
    -------
    dict
        A copy of the metadata dict with keys: ``filename``, ``source``,
        ``url``, ``license``, ``description``.

    Raises
    ------
    DatasetNotFoundError
        If ``name`` is not a registered dataset.
    """
    _validate_name(name)
    return dict(DATASETS[name])


def load_dataset(name: str, **read_csv_kwargs: Any) -> pd.DataFrame:
    """Load a bundled dataset into a pandas DataFrame.

    Parameters
    ----------
    name : str
        Dataset key, e.g. ``"dengue_taiwan"``. See :func:`list_datasets`
        for the full list of valid names.
    **read_csv_kwargs
        Additional keyword arguments forwarded to ``pandas.read_csv``
        (e.g. ``encoding``, ``sep``, ``dtype``).

    Returns
    -------
    pandas.DataFrame

    Raises
    ------
    DatasetNotFoundError
        If ``name`` is not a registered dataset.
    FileNotFoundError
        If the dataset is registered but the CSV file is missing from
        the installed package (e.g. incomplete installation).

    Examples
    --------
    >>> import denguedatasets as dd
    >>> df = dd.load_dataset("dengue_taiwan")   # doctest: +SKIP
    """
    _validate_name(name)
    filename = DATASETS[name]["filename"]

    try:
        resource = pkg_resources.files(_DATA_PACKAGE).joinpath(filename)
        with pkg_resources.as_file(resource) as csv_path:
            if not csv_path.exists():
                raise FileNotFoundError(
                    f"Data file '{filename}' for dataset '{name}' was not "
                    "found in the installed package. Reinstall "
                    "denguedatasets or check 'package_data' configuration."
                )
            return pd.read_csv(csv_path, **read_csv_kwargs)
    except ModuleNotFoundError as exc:
        raise FileNotFoundError(
            f"Could not locate the data directory for denguedatasets: {exc}"
        ) from exc


def _validate_name(name: str) -> None:
    if name not in DATASETS:
        available = ", ".join(list_datasets())
        raise DatasetNotFoundError(
            f"Unknown dataset '{name}'. Available datasets: {available}"
        )
