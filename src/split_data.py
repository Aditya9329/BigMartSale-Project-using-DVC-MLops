import os
import argparse
import yaml

import pandas as pd 
from sklearn.model_selection import train_test_split

from get_data import read_params
from preprocessing import column_imputation,missing_imputation

def split_and_save(config_path):
    config = read_params(config_path)
    train_data_path = config["split_data"]["train_path"]
    test_data_path  = config["split_data"]["test_path"]
    test_size       = config["split_data"]["test_size"]
    random_state    = config["base"]["random_state"]
    processed_data_path  = config["preprocessing"]["processed_data_path"]
    df = pd.read_csv(processed_data_path,sep=",")
    train,test  = train_test_split(df,test_size = test_size,random_state=random_state)
    print("splitting done")
    train.to_csv(train_data_path,sep=",",index=False)
    test.to_csv(test_data_path,sep=",",index=False)
    

    


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    split_and_save(config_path = parsed_args.config)