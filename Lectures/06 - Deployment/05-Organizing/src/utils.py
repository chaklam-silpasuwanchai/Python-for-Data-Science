import logging
import re
import yaml #pip install pyyaml
import torch
import numpy as np
import random
import matplotlib.pyplot as plt

from attrdict   import AttrDict #pip install attrdict
from models.fc  import *
from datasets   import *
from models.cnn import *
from pathlib    import Path

import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

def setup_logger(name, filename, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(filename.with_suffix(".log"), "a")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler) #save to log
    logger.addHandler(logging.StreamHandler()) #but also print to console

    return logger

def set_device():
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print_nicely("device", str(device))
    return device

def set_seed(seed=42):
    torch.backends.cudnn.enabled = False #don't let cuDNN use non-deterministic behavior
    torch.manual_seed(seed)  #for pytorch
    np.random.seed(seed)     #for numpy
    random.seed(seed)        #for python
    print_nicely("seed", seed)

def load_dataset(config, shared_config):
    print_nicely("dataset", config.dataset)
    return globals()[config.dataset](shared_config.batch_size_train, shared_config.batch_size_test)

def load_yaml(config_dir, filename):
    with open(config_dir / filename, "r") as stream:
        config = AttrDict(yaml.safe_load(stream))  #allow us to access the dict as both keys and attributes
    print_nicely("config", filename)
    return config

def get_filename(config_file, datasets_config_file, seed):
    return str(Path(config_file).stem) + "_" + str(Path(datasets_config_file).stem) + "_" + str(seed)

def load_model(config, device):
    class_name = list(config.keys())[0] #e.g., FC
    kwargs = list(config.items())[0][1] #e.g., input_size
    model_class = globals()[class_name] #get class from string
    
    print_nicely("model", class_name)

    model = model_class(**kwargs).to(device)       #make class instance
    
    return model

def print_nicely(text, var):
    logger = logging.getLogger("logger")
    logger.info(f"{text:<15}{var:<15}")
    #< means align to left, and 15 is the width

def plot(train, valid, setup, type):
    
    #for saving figures
    filename = get_filename(setup.config_file, setup.dataset_config_file, setup.seed)
    
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(train, label = f'train {type}')
    ax.plot(valid, label = f'valid {type}')
    plt.legend()
    ax.set_xlabel('updates')
    ax.set_ylabel('loss')
    plt.savefig(f'../figures/{filename}_{type}.png')