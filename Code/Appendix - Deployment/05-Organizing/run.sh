cd src

#set seed
declare -i seed=42

#run experiments of different configs
python main.py -c models/fc1.yaml  -d datasets/normalized.yaml -s  $seed   #run linear -> relu -> linear
python main.py -c models/cnn1.yaml -d datasets/normalized.yaml -s  $seed   #run cnn -> cnn -> linear