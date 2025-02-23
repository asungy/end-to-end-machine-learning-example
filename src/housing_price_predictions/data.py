from housing_price_predictions.logger import LOG
from pathlib import Path
import os
import requests
import shutil
import tarfile

DATA_URL = "https://github.com/ageron/data/raw/main/housing.tgz"


def _share_dir():
    return (
        Path.home()
        .joinpath(".local")
        .joinpath("share")
        .joinpath("housing_price_predictions")
    )

def _housing_dir():
    return  _share_dir().joinpath("housing")


def _remove_housing_dir():
    shutil.rmtree(_housing_dir())


def _download_data():
    housing_dir = _housing_dir()
    if not housing_dir.exists():
        LOG.info(f"Downloading data from {DATA_URL}")
        os.makedirs(housing_dir)
        tgz_path = _share_dir().joinpath("housing.tgz")

        # urllib.request.urlretrieve(DATA_URL, tgz_path)
        response = requests.get(DATA_URL)
        if response.status_code == 200:
            with open(tgz_path, "wb") as f:
                f.write(response.content)
            LOG.info("Downloaded data file successfully.")
        else:
            LOG.error(f"Could not download data file. Status: {response.status_code}")

        housing_tgz = tarfile.open(tgz_path)
        housing_tgz.extractall(path=housing_dir)
        housing_tgz.close()

        os.remove(tgz_path)
    else:
        LOG.debug("Data directory exists.")


def init():
    dir = _share_dir()
    if not dir.exists():
        os.makedirs(dir, exist_ok=True)       
    _download_data()
