import click
from housing_price_predictions.data.files import download_data


@click.command("download")
def command():
    """Downloads housing data."""
    download_data()
