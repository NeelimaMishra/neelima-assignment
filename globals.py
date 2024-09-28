""" This python file contains global variables used throughout the framework """

import os

import yaml

import utility.utilities as utils

utils.decrypt_file()
creds_conf = utils.read_yaml("config/credentials.yaml")

config_data = {}
config_file_path = os.path.abspath("config/credentials.yaml")
with open(config_file_path) as fd:
    config_data = yaml.safe_load(fd)
