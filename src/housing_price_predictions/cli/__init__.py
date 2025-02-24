import click
from housing_price_predictions.cli.check import command as check_command
from housing_price_predictions.cli.clean import command as clean_command
from housing_price_predictions.cli.download import command as download_command


@click.group()
@click.version_option()
def root():
    """CLI for running the housing price predictions example."""
    pass


root.add_command(check_command)
root.add_command(clean_command)
root.add_command(download_command)


def run():
    root()
