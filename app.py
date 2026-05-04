# app.py
import yaml

def load_config(user_input):
#    return yaml.load(user_input, Loader=yaml.Loader)
    return yaml.safe_load(user_input)