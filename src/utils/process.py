import yaml
import os
from pathlib import Path

def process(config_file):
    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    return config