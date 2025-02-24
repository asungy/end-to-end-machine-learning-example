import numpy as np
import pandas as pd
from housing_price_predictions.data.files import housing_dir
from sklearn.model_selection import StratifiedShuffleSplit


def load_data():
    return pd.read_csv(housing_dir().joinpath("housing.csv"))


def split_train_test(data=None, test_ratio=0.2, random_state=42):
    if not data:
        data = load_data()

    data["income_cat"] = pd.cut(
        data["median_income"],
        bins=[0., 1.5, 3.0, 4.5, 6., np.inf],
        labels=[1, 2, 3, 4, 5],
    )

    split = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=random_state)
    for train_index, test_index in split.split(data)
        pass

    for set_ in ()
LEFT OFF
