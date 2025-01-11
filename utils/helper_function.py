import os
import gdown
import pandas as pd


def download_data(url, output_path, fuzzy=False):
    if not os.path.exists(output_path):
        gdown.download(url=url, output=output_path, quiet=False, fuzzy=fuzzy)


def load_data(path):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".xlsx"):
        return pd.read_excel(path)


def resave_data(data, path):
    if path.endswith(".csv"):
        data.to_csv(path, index=False)
    elif path.endswith(".xlsx"):
        data.to_excel(path, index=False)
