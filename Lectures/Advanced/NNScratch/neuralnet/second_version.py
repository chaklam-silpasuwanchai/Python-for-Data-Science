from numpy import ndarray
from typing import List
import numpy as np

#Operations
class Operation(object):

    def __init__(self):
        pass

    def forward(self,
                input_: ndarray,
                inference: bool=False) -> ndarray:  #<----inference

        self.input_ = input_

        self.output = self._output(inference) #<----inference

        return self.output

    def backward(self, output_grad: ndarray) -> ndarray:

        #make sure output and output_grad has same shape
        assert self.output.shape == output_grad.shape

        self.input_grad = self._input_grad(output_grad)

        #input grad must have same shape as input
        assert self.input_.shape == self.input_grad.shape

        return self.input_grad

    def _output(self, inference: bool) -> ndarray:  #<----inference
        raise NotImplementedError()

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        raise NotImplementedError()

class ParamOperation(Operation):
    def __init__(self, param: ndarray):
        super().__init__()  #inherit from parent if any
        self.param = param  #this will be used in _output

    def backward(self, output_grad: ndarray) -> ndarray:
        
        #make sure output and output_grad has same shape
        assert self.output.shape == output_grad.shape

        #perform gradients for both input and param
        self.input_grad = self._input_grad(output_grad)
        self.param_grad = self._param_grad(output_grad)

        assert self.input_.shape == self.input_grad.shape
        assert self.param.shape == self.param_grad.shape

        return self.input_grad

    def _param_grad(self, output_grad: ndarray) -> ndarray:
        raise NotImplementedError()  

class WeightMultiply(ParamOperation):

    def __init__(self, W: ndarray):
        #initialize Operation with self.param = W
        super().__init__(W)

    def _output(self, inference: bool) -> ndarray: #<----inference
        return self.input_ @ self.param

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return output_grad @ self.param.T  #same as last class

    def _param_grad(self, output_grad: ndarray)  -> ndarray:
        return self.input_.T @ output_grad  #same as last class

class BiasAdd(ParamOperation):
    def __init__(self, B: ndarray):
        #initialize Operation with self.param = B.
        assert B.shape[0] == 1  #make sure it's only B
        super().__init__(B)

    def _output(self, inference: bool) -> ndarray: #<----inference
        return self.input_ + self.param

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return np.ones_like(self.input_) * output_grad

    def _param_grad(self, output_grad: ndarray) -> ndarray:
        param_grad = np.ones_like(self.param) * output_grad
        return np.sum(param_grad, axis=0).reshape(1, param_grad.shape[1])


class Linear(Operation):
    def __init__(self) -> None:
        super().__init__()

    def _output(self, inference: bool) -> ndarray:   #<----inference
        return self.input_

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return output_grad


class Sigmoid(Operation):
    def __init__(self) -> None:
        super().__init__()

    def _output(self, inference: bool) -> ndarray:   #<----inference
        return 1.0/(1.0+np.exp(-1.0 * self.input_))

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        sigmoid_backward = self.output * (1.0 - self.output)
        input_grad = sigmoid_backward * output_grad
        return input_grad


class Tanh(Operation):
    def __init__(self) -> None:
        super().__init__()

    def _output(self, inference: bool) -> ndarray:  #<----inference
        return np.tanh(self.input_)

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        return output_grad * (1 - self.output * self.output)


#we have to define Dropout again, so it refers to the new Operation class
class Dropout(Operation):

    def __init__(self,
                 keep_prob: float = 0.8):
        super().__init__()
        self.keep_prob = keep_prob

    def _output(self, inference: bool) -> ndarray: 
        if inference:
            return self.input_ * self.keep_prob  #multiply input by probability
        else:
            #binomial will give us list of 0 and 1s with 1s of probability equal to keep_prob
            self.mask = np.random.binomial(1, self.keep_prob,
                                           size=self.input_.shape)  
            return self.input_ * self.mask

    def _input_grad(self, output_grad: ndarray) -> ndarray:
        #since gradient of 0 is nothing, thus the input_grad is simply whatever output_grad multiply with self.mask
        return output_grad * self.mask

#Layers
class Layer(object):

    def __init__(self,
                 neurons: int) -> None:
        self.neurons = neurons
        self.first = True
        self.params: List[ndarray] = []
        self.param_grads: List[ndarray] = []
        self.operations: List[Operation] = []

    def _setup_layer(self, input_: ndarray) -> None:
        pass

    def forward(self, input_: ndarray,
                inference=False) -> ndarray:   #<--------added

        if self.first:
            self._setup_layer(input_)
            self.first = False

        self.input_ = input_

        for operation in self.operations:
            input_ = operation.forward(input_, inference)   #<------added inference as param

        self.output = input_

        return self.output

    def backward(self, output_grad: ndarray) -> ndarray:

        assert self.output.shape == output_grad.shape

        for operation in self.operations[::-1]:
            output_grad = operation.backward(output_grad)

        input_grad = output_grad
        
        assert self.input_.shape == input_grad.shape

        self._param_grads()

        return input_grad

    def _param_grads(self) -> None:

        self.param_grads = []
        for operation in self.operations:
            if issubclass(operation.__class__, ParamOperation):
                self.param_grads.append(operation.param_grad)

    def _params(self) -> None:

        self.params = []
        for operation in self.operations:
            if issubclass(operation.__class__, ParamOperation):
                self.params.append(operation.param)

class Dense(Layer):
    def __init__(self, neurons: int,
                 activation: Operation = Sigmoid(),
                 dropout: float = 1.0,  #<---add default dropout as 1.0 which means all values are kept
                 weight_init: str = "glorot"):
        #define the desired non-linear function as activation
        super().__init__(neurons)
        self.activation = activation
        self.weight_init = weight_init 
        self.dropout = dropout  #<----added

    def _setup_layer(self, input_: ndarray):
        #in case you want reproducible results
        if self.seed:
            np.random.seed(self.seed)

        num_in = input_.shape[1]

        if self.weight_init == "glorot":
            scale = 2/(num_in + self.neurons)
        else:
            scale = 1.0   
            
        self.params = []
        
        # weights
        self.params.append(np.random.normal(loc=0,
                                            scale=scale,
                                            size=(num_in, self.neurons)))

        # bias
        self.params.append(np.random.normal(loc=0,
                                            scale=scale,
                                            size=(1, self.neurons)))

        self.operations = [WeightMultiply(self.params[0]),
                           BiasAdd(self.params[1]),
                           self.activation]
        
        if self.dropout < 1.0:
            self.operations.append(Dropout(self.dropout))

#Loss
class Loss(object):
   
    def __init__(self):
        pass

    def forward(self, prediction: ndarray, target: ndarray) -> float:
        assert prediction.shape == target.shape

        self.prediction = prediction
        self.target = target
        
        #self._output will hold the loss function
        loss_value = self._output()

        return loss_value

    def backward(self) -> ndarray:

        self.input_grad = self._input_grad()

        assert self.prediction.shape == self.input_grad.shape

        #input_grad will hold the gradient of the loss function
        return self.input_grad

    def _output(self) -> float:
        raise NotImplementedError()

    def _input_grad(self) -> ndarray:
        raise NotImplementedError()

class MeanSquaredError(Loss):

    def __init__(self):
        super().__init__()

    def _output(self) -> float:
        loss = (
            np.sum(np.power(self.prediction - self.target, 2)) / 
            self.prediction.shape[0]
        )

        return loss

    def _input_grad(self) -> ndarray:
        return 2.0 * (self.prediction - self.target) / self.prediction.shape[0]

class SoftmaxCrossEntropy(Loss):
    def __init__(self, eps: float=1e-9):
        super().__init__()
        self.eps = eps

    def _output(self) -> float:
        
        # applying the softmax function to each row (observation)
        softmax_preds = self.softmax(self.prediction, axis=1)

        # clipping the softmax output to prevent numeric instability
        #numpy.clip(a, a_min, a_max, out=None, **kwargs)
        #To prevent extremely large loss values that could lead to numeric instability, 
        #we’ll clip the output of the softmax function to be no less than 10–7 and no greater than 10^7
        self.softmax_preds = np.clip(softmax_preds, self.eps, 1 - self.eps)

        # actual loss computation
        softmax_cross_entropy_loss = (
            -1.0 * self.target * np.log(self.softmax_preds) - \
                (1.0 - self.target) * np.log(1 - self.softmax_preds)
        )
        
        #return average loss
        return np.sum(softmax_cross_entropy_loss) / self.prediction.shape[0]

    def _input_grad(self) -> ndarray:
        #return average grad
        return (self.softmax_preds - self.target) / self.prediction.shape[0]

    def softmax(self, x, axis=None):
        #keepdims so that this number can be broadcasted and divided
        return np.exp(x) / np.sum(np.exp(x), axis=axis, keepdims=True)

#Neural Network
class NeuralNetwork(object):
    def __init__(self, 
                 layers: List[Layer],
                 loss: Loss,
                 seed: int = 1):
        self.layers = layers
        self.loss = loss
        self.seed = seed
        if seed:
            for layer in self.layers:
                setattr(layer, "seed", self.seed)        
  
    def forward(self, X_batch: ndarray,
                inference=False) ->  ndarray:   #<----added inference as param

        X_out = X_batch
        for layer in self.layers:
            X_out = layer.forward(X_out, inference)  #<----added inference as param

        return X_out
    
    def backward(self, loss_grad: ndarray):
        grad = loss_grad
        for layer in reversed(self.layers):
            grad = layer.backward(grad)
            
            #you may wonder why I did not return anything
            #it's because in Layer.backward, it is appending this value to param_grads to each layer
            #this return "grad" is simply something it returns
  
    def train_batch(self,
                    X_batch: ndarray,
                    y_batch: ndarray,
                    inference: bool = False) -> float:  #<-----added inference as param

        prediction = self.forward(X_batch, inference)  #<----added inference as param

        batch_loss = self.loss.forward(prediction, y_batch)
        loss_grad = self.loss.backward()

        self.backward(loss_grad)

        return batch_loss
    
    def params(self):
        #get the parameters for the network
        #use for updating w and b
        for layer in self.layers:
            #equivalent for-loop yield
            #yield is different from return is that
            #it will return a sequence of values
            yield from layer.params

    def param_grads(self):
        #get the gradient of the loss with respect to the parameters
        #for the network
        #use for updating w and b
        for layer in self.layers:
            yield from layer.param_grads

#Optimizer
#parent class
class Optimizer(object):
    def __init__(self,
                 lr: float = 0.01,
                 final_lr: float = 0,
                 decay_type: str = 'exponential'):
        self.lr = lr
        self.final_lr = final_lr  #<----added
        self.decay_type = decay_type #<----added

    def _setup_decay(self):  #<----added

        if not self.decay_type:
            return
        elif self.decay_type == 'exponential':
            self.decay_per_epoch = np.power(self.final_lr / self.lr,
                                       1.0 / (self.max_epochs - 1))
        elif self.decay_type == 'linear':
            self.decay_per_epoch = (self.lr - self.final_lr) / (self.max_epochs - 1)

    def _decay_lr(self): #<----added

        if not self.decay_type:
            return

        if self.decay_type == 'exponential':
            self.lr *= self.decay_per_epoch

        elif self.decay_type == 'linear':
            self.lr -= self.decay_per_epoch

    def step(self, epoch: int = 0):  #<----added epoch info

        for (param, param_grad) in zip(self.net.params(),
                                       self.net.param_grads()):
            self._update_rule(param=param,
                              grad=param_grad)

    def _update_rule(self, **kwargs):
        raise NotImplementedError()

#Stochasitc gradient descent optimizer.  
class SGD(Optimizer): 
    def __init__(self, lr: float = 0.01):
        super().__init__(lr)

    def step(self):
        #params hold w and b
        #param_grads hold their gradients
        for (param, param_grad) in zip(self.net.params(),
                                       self.net.param_grads()):

            param -= self.lr * param_grad


class SGDMomentum(Optimizer):
    def __init__(self,
                 lr: float = 0.01,
                 final_lr: float = 0,   #<----added
                 decay_type: str = None,   #<------added
                 momentum: float = 0.9):
        super().__init__(lr, final_lr, decay_type)   #<---changed
        self.momentum = momentum
        self.first = True

    def step(self):
        if self.first:
            self.velocities = [np.zeros_like(param)
                               for param in self.net.params()]
            self.first = False

        for (param, param_grad, velocity) in zip(self.net.params(),
                                                 self.net.param_grads(),
                                                 self.velocities):
            self._update_rule(param=param,
                              grad=param_grad,
                              velocity=velocity)

    def _update_rule(self, **kwargs):

            # Update velocity
            kwargs['velocity'] *= self.momentum
            kwargs['velocity'] += self.lr * kwargs['grad']

            # Use this to update parameters
            kwargs['param'] -= kwargs['velocity']

#Trainer
from copy import deepcopy
from typing import Tuple

class Trainer(object):
    #NeuralNetwork and Optimizer as attributes
    def __init__(self,
                 net: NeuralNetwork,
                 optim: Optimizer):
        #Requires a neural network and an optimizer in order for 
        #training to occur. 
        self.net = net
        self.optim = optim
        self.best_loss = 1e9  #use for comparing the least amount of loss
        
        #Assign the neural network as an instance variable to 
        #the optimizer when the code runs
        setattr(self.optim, 'net', self.net)
    

    # helper function for shuffling
    def permute_data(self, X, y):
        perm = np.random.permutation(X.shape[0])
        return X[perm], y[perm]

    # helper function for generating batches
    def generate_batches(self,
                         X: ndarray,
                         y: ndarray,
                         size: int = 32) -> Tuple[ndarray]:
        #X and y should have same number of rows
        assert X.shape[0] == y.shape[0]

        N = X.shape[0]

        for i in range(0, N, size):
            X_batch, y_batch = X[i:i+size], y[i:i+size]
            #return a generator that can be loop
            yield X_batch, y_batch

            
    def fit(self, X_train: ndarray, y_train: ndarray,
            X_test: ndarray, y_test: ndarray,
            epochs: int=100,
            eval_every: int=10,
            batch_size: int=32,
            seed: int = 20200720,
            restart: bool = True):
        
        
        setattr(self.optim, 'max_epochs', epochs)
        self.optim._setup_decay()

        np.random.seed(seed)
        
        #for resetting
        if restart:
            for layer in self.net.layers:
                layer.first = True

            self.best_loss = 1e9
        
        #Fits the neural network on the training data for a certain 
        #number of epochs.
        for e in range(epochs):
            
            if (e+1) % eval_every == 0:
                
                # for early stopping
                # deepcopy is a hardcopy function that make sure it construct a new object (copy() is a shallow copy)
                last_model = deepcopy(self.net)

            X_train, y_train = self.permute_data(X_train, y_train)

            batch_generator = self.generate_batches(X_train, y_train,
                                                    batch_size)

            for (X_batch, y_batch) in batch_generator:

                self.net.train_batch(X_batch, y_batch)

                self.optim.step()
            
            #Every "eval_every" epochs, it evaluated the neural network 
            #on the testing data.
            if (e+1) % eval_every == 0:

                test_preds = self.net.forward(X_test, inference=True) #<----inference   #<---make sure validation does not use dropout
                loss = self.net.loss.forward(test_preds, y_test)

                if loss < self.best_loss:
                    print(f"Validation loss after {e+1} epochs is {loss:.3f}")
                    self.best_loss = loss
                #if the validation loss is not lower, it stop and perform early stopping
                else:
                    print(f"""Loss increased after epoch {e+1}, final loss was {self.best_loss:.3f}, using the model from epoch {e+1-eval_every}""")
                    self.net = last_model
                    # ensure self.optim is still updating self.net
                    setattr(self.optim, 'net', self.net)
                    break
            
            #call this at the end of each epoch
            if self.optim.final_lr:
                self.optim._decay_lr() 