from housing_price_predictions.data.training import split_train_test
import matplotlib.pyplot as plt
import os
import pandas as pd


def geographical_scatter_plot(data: pd.DataFrame, filename: str):
    """Creates a file that geographically visualizes the location of median housing prices."""
    data.plot(
        title="Median Housing Prices vs Location and Population Density",
        kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.4,
        s=data["population"] / 100,
        label="population",
        figsize=(10, 7),
        c="median_house_value",
        cmap=plt.get_cmap("jet"),
        colorbar=True,
    )
    plt.savefig(filename)


def training_geographical_scatter_plot():
    train_set, _ = split_train_test()
    geographical_scatter_plot(
        train_set, os.path.join(os.getcwd(), "training_geographical_scatter_plot.png")
    )


def scatter_matrix(data: pd.DataFrame, attributes: [str], filename: str):
    pd.plotting.scatter_matrix(data[attributes], figsize=(12, 8))
    plt.savefig(filename)


def create_scatter_matrix_image():
    train_set, _ = split_train_test()
    scatter_matrix(
        train_set,
        ["median_house_value", "median_income", "total_rooms", "housing_median_age"],
        "scatter_matrix.png",
    )
