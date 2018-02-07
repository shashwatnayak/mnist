import network
import mnist_loader
net = network.Network([784,30,10])
training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
#Solved
