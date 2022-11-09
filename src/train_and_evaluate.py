## load train and test data
## train algorithm
## save the metrics and params

import os
import pandas as pd
import pickle
import argparse
import sys
from sklearn.metrics import mean_squared_error,mean_absolute_error
from get_data import read_params 
import joblib
import json
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder





def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path  = config["split_data"]["train_path"]

    train_data_path = config["split_data"]["test_path"]

    model_dir       = config["model_dir"]

    random_state    = config["base"]["random_state"]

    max_depth       = config["estimators"]["RandomForestRegressor"]["params"]["max_depth"]

    n_jobs          = config["estimators"]["RandomForestRegressor"]["params"]["n_jobs"]

    max_leaf_nodes  = config["estimators"]["RandomForestRegressor"]["params"]["max_leaf_nodes"]

    n_estimators    = config["estimators"]["RandomForestRegressor"]["params"]["n_estimators"]

    min_impurity_decrease = config["estimators"]["RandomForestRegressor"]["params"]["min_impurity_decrease"]

    # print(  train_data_path)
    # print(model_dir)
    # print(random_state)
    # print(max_depth)
    # print(n_jobs)
    # print(max_leaf_nodes)
    # print(n_estimators)
    # print(min_impurity_decrease)

    target = [config["base"]["target_col"]]
    train = pd.read_csv(train_data_path,sep=",")
    test  = pd.read_csv(test_data_path,sep=",")

    train_y = train[target]
    test_y  = test[target]

    train_x = train.drop(target,axis=1)
    test_x  = test.drop(target,axis=1)

    # tranforming
    transformer = ColumnTransformer(transformers=[
    ('tnf1',OneHotEncoder(handle_unknown='ignore',sparse=False,drop="first"),['item_identifier','item_fat_content','item_type','outlet_identifier']),
    ('tnf2',OrdinalEncoder(categories=[['Small','Medium','High'],['Tier 1','Tier 2','Tier 3'],['Grocery Store','Supermarket Type1','Supermarket Type2','Supermarket Type3']]),
     ['outlet_size','outlet_location_type','outlet_type'])
    ] ,remainder="passthrough")



    # start pickling a model
    # pickle.dump(transformer, open('transform', 'wb'))------------

    # transformer = pickle.load(open('./notebooks/tranformer_model.pkl', 'rb'))
    print("--------TRANSFORMER:- READY----------------")
    # vect  =  pickle.load(open('./vectorizer/vectorize.pickle', 'rb'))
    train_trfd = transformer.fit_transform(train_x)
    pickle.dump(train_trfd, open('transform', 'wb'))
    test_trfd  = transformer.transform(test_x)
    # print(train_trfd)
    print("-----------DATA TRANSFORMED----------------")

    print(train_trfd)
    print(test_trfd)
    print("------------START TRAINING MODEL-----------")
    rf = RandomForestRegressor(max_depth = max_depth,
                                n_estimators = n_estimators,
                                # n_jobs = n_jobs,
                                # max_leaf_nodes = max_leaf_nodes,
                                min_impurity_decrease = min_impurity_decrease)


    rf.fit(train_trfd,train_y)
    print("----------TRANING IS DONE-----------------")
    y_pred = rf.predict(test_trfd)
    mse = mean_squared_error(test_y , y_pred)
    rmse = np.sqrt(mse)

    print("MSE: ",mse)
    print("RMSE: ",rmse)

    
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file,"w") as f:
        scores = {
            'mse':mse,
            'rmse':rmse
        }

        json.dump(scores,f,indent = 4)
    with open(params_file,"w") as f:
        params = {
            'random_state':random_state,
            'max_depth':max_depth,
            'min_impurity_decrease':min_impurity_decrease,
            'n_estimators':n_estimators
        }
        json.dump(params,f,indent = 4)


    os.makedirs(model_dir,exist_ok=True)
    model_path = os.path.join(model_dir,"model.joblib")
    joblib.dump(rf, model_path)
    print("------------TRAINING STAGE AND EVALUATION STAGE COMPLETED-----------")




    





if __name__ == "__main__":
        args = argparse.ArgumentParser()
        args.add_argument("--config",default = "params.yaml")
        parsed_args = args.parse_args()
        train_and_evaluate(config_path = parsed_args.config)