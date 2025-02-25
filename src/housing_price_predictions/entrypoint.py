from housing_price_predictions import cli
from housing_price_predictions.data.files import init_dir


def main():
    init_dir()
    cli.run()
