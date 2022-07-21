import torch.optim  as optim
import utils
import argparse

from datetime       import datetime
from train          import train_eval, test
from torch          import nn
from pathlib        import Path
from setup          import Setup

config_dir = Path("../configs")
log_dir    = Path("../logs")

def _run_experiment(config_file, dataset_config_file, seed):
    
    #0. set logger
    filename = utils.get_filename(config_file, dataset_config_file, seed)    
    logger = utils.setup_logger("logger", log_dir / filename)
    
    logger.info("===Start Experiment===")
    utils.print_nicely("time", datetime.now().strftime("%d:%b:%Y-%H:%M:%S"))
    
    #1. load config
    config         = utils.load_yaml(config_dir, config_file)  #config of that architecture
    dataset_config = utils.load_yaml(config_dir, dataset_config_file)  #shared config
    shared_config  = utils.load_yaml(config_dir, "shared_config.yaml")  #shared config

    #2. set seeds and device
    utils.set_seed(seed)
    device = utils.set_device()
    
    #3. load dataset
    train_loader, val_loader, test_loader = utils.load_dataset(dataset_config, shared_config)

    #4. load model
    model = utils.load_model(config, device)
    
    #5. set optimizer and loss function
    optimizer = optim.SGD(model.parameters(), lr=shared_config.learning_rate, momentum=shared_config.momentum)
    criterion = nn.CrossEntropyLoss()
    
    #Optional: create a class instance, instead of passing arguments
    setup = Setup(bool_reshape = config.bool_reshape, 
                  n_epochs = shared_config.n_epochs, 
                  train_loader = train_loader, 
                  val_loader = val_loader,
                  test_loader = test_loader,
                  model = model,
                  criterion = criterion,
                  optimizer = optimizer,
                  device = device,
                  config_file = config_file,
                  dataset_config_file = dataset_config_file,
                  seed = seed)             
        
    #6. train model
    train_losses, train_accs, valid_losses, valid_accs =  train_eval(setup)
    
    #7. eval model
    test(setup)
        
    #8. visualize results
    utils.plot(train_losses, valid_losses, setup, "loss")
    utils.plot(train_accs,   valid_accs  , setup, "acc" )

if __name__ == "__main__":
  # initialize ArgumentParser class of argparse
  parser = argparse.ArgumentParser()
 
  # add different arguments and their types
  parser.add_argument('-c', '--config_file', type=str, required=True)
  parser.add_argument('-d', '--dataset_config_file', type=str, required=True)
  parser.add_argument('-s', '--seed', type=int, required=True)

  # read arguments from command line
  args = parser.parse_args()
    
  # run with arguments specified by command line arguments
  _run_experiment(
      config_file=args.config_file,
      dataset_config_file=args.dataset_config_file,
      seed = args.seed
      )