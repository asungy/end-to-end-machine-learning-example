import click
import sys
from pathlib import Path
from housing_price_predictions.data import housing_dir, housing_dir_size
from housing_price_predictions.logger import LOG


@click.command("check")
def command():
    """Checks whether the `housing/` directory is downloaded."""
    if not Path(housing_dir()).exists():
        LOG.error("`housing/` directory does not exist.")
        sys.exit(1)

    LOG.info(f"`housing/` directory size: {housing_dir_size()}")
