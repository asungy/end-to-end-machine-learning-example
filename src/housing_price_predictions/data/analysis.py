import pandas as pd


def correlation_matrix(data: pd.DataFrame):
    copy = data.drop("ocean_proximity", axis=1)
    return copy.corr()


def correlation(data: pd.DataFrame, key: str):
    return correlation_matrix(data)[key].sort_values(ascending=False)
