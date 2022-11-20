class Setup(object):
    """docstring for Setup."""
    def __init__(self, bool_reshape, n_epochs, train_loader, val_loader, test_loader,
                model, criterion, optimizer, device, config_file, dataset_config_file, seed):
        super(Setup, self).__init__()
        self.bool_reshape = bool_reshape
        self.n_epochs = n_epochs
        self.train_loader = train_loader
        self.val_loader = val_loader
        self.test_loader = test_loader
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.device = device
        self.config_file = config_file
        self.dataset_config_file = dataset_config_file
        self.seed = seed