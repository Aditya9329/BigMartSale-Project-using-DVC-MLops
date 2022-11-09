import os
import yaml
import argparse
import pandas as pd
from get_data import read_params,get_data
import logging
import numpy as np



logging.basicConfig(filename="application_log.txt",
                            format='%(asctime)s %(message)s',
                            filemode='w')


logger = logging.getLogger()

def column_imputation(config_path):
    try:
       
        config = read_params(config_path)
        print("column imputation running...")
        # print(config)
        raw_data_path = config["load_data"]["raw_dataset_csv"]
        data = pd.read_csv(raw_data_path,sep=",")
        # print(data.columns)
        data.columns = data.columns.str.lower()
        # print(data.isnull().mean()*100)
        return data
    except Exception as e:
        print(str(e))


def missing_imputation(config_path):
    try:
        data  = column_imputation(config_path)
        # print("He;;p")
        # print(data)
        
        data['item_weight'] = data['item_weight'].replace(np.nan,data['item_weight'].mean())
        # print(data['item_weight'].head(2))
        data['outlet_size'] = data['outlet_size'].replace(np.nan,'Medium')
        # print("outlet",data['outlet_size'].head(2))
        data['item_fat_content'] = data['item_fat_content'].replace('LF','Low Fat')
        data['item_fat_content'] = data['item_fat_content'].replace('low fat','Low Fat')
        data['item_fat_content'] = data['item_fat_content'].replace('reg','Regular')
        # print(data)
        print("missing imputor running...")
        config = read_params(config_path)
        preprocessed_data_path = config["preprocessing"]["processed_data_path"]  
        print("about to complete.....")
        data.to_csv(preprocessed_data_path,sep=",",index=False)     

        # print(data.isnull().mean()*100)

    except Exception as e:
        print("error",str(e)) 




    



    





if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    data  = missing_imputation(config_path = parsed_args.config)
    # print(data)