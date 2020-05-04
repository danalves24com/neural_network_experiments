import numpy as np
from matplotlib import pyplot as plt
np.random.seed(0)
X = [[1, 2 ,3, 2.5],
    [2.0, 5.0, 1.0, 2.0], 
    [1.5, 2.7, 3.3, 0.8]]

class Layer_Dense:
    def __init__(self, n_inputs, n_neur):
        self.weights =np.random.randn(n_inputs, n_neur)    
        self.biases = np.zeros((1, n_neur))
    def forward(self, inp):
        self.output = np.dot(inp, self.weights) + self.biases

layer1 = Layer_Dense(4, 5)
layer2 = Layer_Dense(5, 3)
layer3 = Layer_Dense(3, 8)
layer1.forward(X)
print(layer1.output)
layer2.forward(layer1.output)
print(layer2.output)
layer3.forward(layer2.output)
print(layer3.output)

plt.plot(X)
plt.show()
plt.plot(layer3.output)
plt.show()