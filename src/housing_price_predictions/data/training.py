import numpy as np
import pandas as pd
from housing_price_predictions.data.files import housing_dir
from sklearn.model_selection import StratifiedShuffleSplit
from typing import Tuple


def load_data() -> pd.DataFrame:
    """Loads the housing data."""
    return pd.read_csv(housing_dir().joinpath("housing.csv"))


def split_train_test(
    data: pd.DataFrame | None = None, test_ratio: float = 0.2, random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Splits the provided data into training and testing sets."""

    if not data:
        data = load_data()

    data["income_cat"] = pd.cut(
        data["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )

    split = StratifiedShuffleSplit(
        n_splits=1, test_size=test_ratio, random_state=random_state
    )
    strat_train_set = None
    strat_test_set = None
    for train_index, test_index in split.split(data, data["income_cat"]):
        strat_train_set = data.loc[train_index]
        strat_test_set = data.loc[test_index]

    for set_ in (strat_train_set, strat_test_set):
        set_.drop("income_cat", axis=1, inplace=True)

    return strat_train_set, strat_test_set


def separate_predictor_and_labels(data: pd.DataFrame, predictor_key: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    return data.drop(predictor_key, axis=1), data[predictor_key].copy()
