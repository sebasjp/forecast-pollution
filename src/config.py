import yaml

with open("config.yaml") as file:
    params = yaml.safe_load(file)

class Config:
    INPUT_PATH = params["data"]["path"]
    MODEL = params["train"]["model"]
    SEED = params["train"]["hyperparameters"]["seed"]