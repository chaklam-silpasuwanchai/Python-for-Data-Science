# Organizing Machine Learning Projects
The repository aims to teach my students how to best organize your ML code for efficiency and to facilitate experiments.  This example is mostly for PyTorch but can be adjusted.  It contains backbone folders and some sample files for illustration.

Note:  You can use something like Wandb to simplify some of the code I have here, but my main point is to explain some good practices and techniques.

## Key idea

When we build our project, we don't want to use a lot of our memory.  Basically, we want to run as mindlessly as possible.  We don't want to remember which models we just run, how many epochs, etc. 

Also, we want to repeat ourself as little as possible.  When we experiment, we want to change as little code as possible.    Everything should be as well-isolated.  

## Sample structure

Here is a sample project structure you can start with.

    +-- data                    
    |   +-- raw                     #raw dataset you get from internet (non-modified)
    |       +-- subj1.csv
    |   +-- processed               #preprocessed dataset; ready to be used
    |       +-- subj1.npy       
    +-- src                         #contains .py files
    |   +-- datasets.py             #for laoding datasets
    |   +-- main.py                 #main file running
    |   +-- train.py                #for training and evaluation
    |   +-- utils.py                #useful utilities (used across projects)
    |   +-- setup.py                #optional; create a class object for sending multiple components across functions.
    |   +-- models                  #containing architecture implementation
    |       +-- cnn.py  
    |       +-- fc.py
    +-- configs                     #contain configurations for datasets and models
    |   +-- models
    |       +-- cnn.yaml
    |       +-- fc.yaml
    |   +-- datasets
    |       +-- normalized.yaml
    |       +-- augmented.yaml
    +-- saved                       #for saving models
    |   +-- sample_model1.pt
    +-- figures                     #save figures
    +-- logs                        #keep logs
    +-- run.sh                      #for running multiple "main.py" experiments
    requirements.txt                #can use pipreqs .
    .gitignore

The main file that the user will interact is `run.sh`.  The `run.sh` will execute `main.py` which will in turn execute multiple `train.py` with different configurations.  `.yaml` will define which network architecture, hyperparameters, and datasets file to use. 

Optionally, you can also have these folders:

    +-- docker                  #contains docker related files, e.g Dockerfile
    |   +-- Dockerfile
    +-- api
    |   +-- api.py              #expose APIs for production
    +-- logs
    |   +-- sample-log

## Sample usage

For simplicity, we just use the MNIST as case study.

Run on the terminal 

    sh run.sh

Looking inside `run.sh`

```shell
cd src

#set seed
declare -i seed=42

#run experiments of different configs
python main.py -c models/fc1.yaml  -d datasets/normalized.yaml -s  $seed 
python main.py -c models/cnn1.yaml -d datasets/normalized.yaml -s  $seed  
```

This file simply go in the `src` directory, create an `integer` of 42, then call the `main.py` with given configs.

Looking inside `main.py`

```python
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
```

The `main.py` will basically run `_run_experiment` with the given config file.

## Why this structure is good?

Normally, to add or change somethign, it requires tremendous effort since our code complexity skyrockets after several months.

Here, to add any new model or preprocessing pipeline, the step we take is easy:

1.  Add new model in `src/models` folder or
2.  Add new preprocessing pipeline in `src/datasets.py`
3.  Simply add a new config under `configs` folder, specifying which model / preprocessing pipeline to use.

That's it!!   All results will be kept in:

- `logs`: all epoch acc and loss
- `figures`: figures for acc and loss
- `saved`:  best model

## Can I use this for my project?

If you are beginners, I think this file structure is quite **decent to start with**.  It forces you to be clean and systematic. 

Once you do more, you will realize **some part has to change**, which is the exact intention of this sample structure.   So don't hesitate to play around.  There are many more tricks that I leave there, for example, using `globals` to map string to function/class, using class `setup.py` to wrap arguments, 

Last, by using this structure, you gain many **benefits**:
- people out there can understand your code better, because almost everyone use similar structure like this
- more systematic and less prone to errors during experimentation
- more impressive, when you want to get a job....

One last thing, there is many experimentation tool nowadays, such as `wandb` or `tensorboard`.  Feel free to try to integrate to this structure; i.e., it basically replaces our `logging`.

## Enjoy coding~