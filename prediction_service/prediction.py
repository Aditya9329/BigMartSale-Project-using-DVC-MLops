import yaml
import joblib
import pickle
params_path = 'params.yaml'

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


def predict(data):
    # config = read_params(params_path)
    # print(data)
    transformer = pickle.load(open('transformer_model.sav','rb'))
    data = transformer.transform(data)
    print(data)
    return data
    # print(config)
    # model_dir_path = config["model_dir"]
    # model = joblib.load(model_dir_path)

    # prediction = model.predict(data)
    # print(prediction)

