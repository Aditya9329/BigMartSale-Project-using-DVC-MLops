import os 
import argparse
import pandas as pd
import yaml 


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config



def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    print(data_path)

    df = pd.read_csv(data_path,sep=",")
    print(df.head())
    return df







if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    print(parsed_args.config)
    print(parsed_args)
    data = get_data(config_path = parsed_args.config)
