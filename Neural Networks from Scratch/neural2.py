import numpy 
numpy.random.seed(0)
class neural_Laier:
    def __init__(self,n_inputs,n_neurans):
        self.weights=numpy.random.randn(n_inputs,n_neurans)/10
        self.biases=numpy.zeros((1,n_neurans))
    def forward(self,inputs):
        self.output=numpy.dot(inputs,self.weights)+self.biases
layer1=neural_Laier(3,5)
layer2=neural_Laier(5,5)
layer3=neural_Laier(5,2)

X=numpy.random.rand(32,3)


layer1.forward(X)
layer2.forward(layer1.output)
layer3.forward(layer2.output)
print(layer3.output)