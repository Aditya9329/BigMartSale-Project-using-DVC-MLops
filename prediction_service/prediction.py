import yaml
import joblib
import pickle
import argparse
# params_path = 'params.yaml'

# def read_params(config_path):
#     with open(config_path) as yaml_file:
#         config = yaml.safe_load(yaml_file)
#     return config


# def predict(config_path):
#     config = read_params(config_path)
#     # print(data)
#     model_dir_path = config["model_dir"]
#     model = joblib.load(model_dir_path)
#     prediction = model.predict(data)
#     print(prediction)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default = "params.yaml")
    parsed_args = args.parse_args()
    # predict(config_path = parsed_args.config)