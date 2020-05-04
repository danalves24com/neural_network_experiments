inputs = [1, 2 ,3, 2.5]
weights=[[0.2, 0.8, -0.5, 1.0],
        [0.5, -0.91, 0.26, -0.5],
        [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3 , 0.5]




layer_Outputs = list()
for neuron_W, neuron_B in zip(weights, biases):
    neuron_Out = 0
    print(zip(weights, biases))
    for n_in, weight in zip(inputs, neuron_W):
        neuron_Out+=n_in*weight
    neuron_Out+=neuron_B
    layer_Outputs.append(neuron_Out)
print(layer_Outputs) 