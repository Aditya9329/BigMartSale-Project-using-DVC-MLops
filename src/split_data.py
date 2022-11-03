import os
import argparse
import yaml

import pandas as pd 
from sklearn.model_selection import train_test_split

from get_data import read_params
from preprocessing import column_imputation,missing_imputation

def split_and_save(config_path):
    config = read_params(config_path)
    data_to_process = missing_imputation(config)
    print(data_to_process)

    




if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    split_and_save(config_path = parsed_args.config)