import click
import housing_price_predictions.cli.check
import housing_price_predictions.cli.clean
import housing_price_predictions.cli.download

@click.group()
@click.version_option()
def root():
    """CLI for running the housing price predictions example."""
    pass

root.add_command(check.command)
root.add_command(clean.command)
root.add_command(download.command)

def run():
    root()
