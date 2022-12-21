import torch, torchvision
from torchvision import transforms, datasets

def normalized(batch_size_train, batch_size_test):
    
    # define the preprocessing
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])
    
    # get the train and test dataset
    train_dataset = datasets.MNIST(root = '../data/processed', train=True,  transform = transform, download=True)
    test_dataset  = datasets.MNIST(root = '../data/processed', train=False, transform = transform, download=True)

    # define the train and val set
    lengths = [int(len(train_dataset) * 0.8), int(len(train_dataset) * 0.2)]
    train_set, val_set = torch.utils.data.random_split(train_dataset, lengths)
        
    # make the loader
    train_loader = torch.utils.data.DataLoader(train_set,    batch_size=batch_size_train,shuffle=True)
    val_loader   = torch.utils.data.DataLoader(val_set,      batch_size=batch_size_test, shuffle=True)
    test_loader  = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size_test, shuffle=True)

    return train_loader, val_loader, test_loader