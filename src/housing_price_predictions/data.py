from housing_price_predictions.logger import LOG
from pathlib import Path
import os
import requests
import shutil
import tarfile
import pandas as pd

DATA_URL = "https://github.com/ageron/data/raw/main/housing.tgz"


def _share_dir():
    return (
        Path.home()
        .joinpath(".local")
        .joinpath("share")
        .joinpath("housing_price_predictions")
    )

def housing_dir():
    return _share_dir().joinpath("housing")


def remove_housing_dir():
    shutil.rmtree(housing_dir())


def download_data():
    if not housing_dir().exists():
        LOG.info(f"Downloading data from {DATA_URL}")
        tgz_path = _share_dir().joinpath("housing.tgz")

        response = requests.get(DATA_URL)
        if response.status_code == 200:
            with open(tgz_path, "wb") as f:
                f.write(response.content)
            LOG.info("Downloaded data file successfully.")
        else:
            LOG.error(f"Could not download data file. Status: {response.status_code}")

        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=_share_dir())
        housing_tgz.close()
        os.remove(tgz_path)
    else:
        LOG.debug("Data directory already exists.")


def load_data():
    return pd.read_csv(housing_dir().joinpath("housing.csv"))


def housing_dir_size():
    size = 0
    for dirpath, dirnames, filenames in os.walk(housing_dir()):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            size += os.path.getsize(file_path)
    return size


def init():
    """Initialize directory to store data."""
    dir = _share_dir()
    if not dir.exists():
        os.makedirs(dir, exist_ok=True)       
