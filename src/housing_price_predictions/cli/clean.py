import click
from housing_price_predictions.data.files import remove_housing_dir
from housing_price_predictions.logger import LOG


@click.command("clean")
def command():
    """Removes the `housing/` directory."""
    LOG.info("Deleting `housing/` directory.")
    remove_housing_dir()
    LOG.info("`housing/` directory deleted.")
