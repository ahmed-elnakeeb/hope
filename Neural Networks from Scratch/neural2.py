import numpy
import sys
import timeit

numpy.random.seed(0)

class neural_Layer:
    def __init__(self,n_inputs,n_neurans):
        self.weights=numpy.random.randn(n_inputs,n_neurans)/10
        self.biases=numpy.ones((1,n_neurans))
    def forward(self,inputs):
        self.output=numpy.dot(inputs,self.weights)+self.biases
    def __str__(self):
        x="\n"+str(self.weights)+"biases\n"+str(self.biases)
        return (x)
class activation:

    @staticmethod
    def ReLU(inputs):
        return(numpy.maximum(0,inputs))
    @staticmethod
    def softmax(x):
        """Compute softmax values for each sets of scores in x."""
        return numpy.exp(x) / numpy.sum(numpy.exp(x), axis=0)
class Network:
    def __init__(self,n_inputs,n_outputs,act_fun,*args):
        """
        args should be i the format of (...,number of layers ,layer size,
        number of layers ,layer size,..)
        """
        if (len(args)%2==0 and len(args)>0 and act_fun=="relu"):

            pass
        else:
            sys.exit()
        inputs=n_inputs
        self.layers=[]

        for i in range(int(len(args)/2)):
            for _ in range(args[2*i]):
                self.layers.append(neural_Layer(inputs,args[2*i+1]))
                inputs=args[2*i+1]
        self.outputLayr=neural_Layer(inputs,n_outputs)

    def forward_All(self,X:list):
        next=X
        for layer in self.layers:
            layer.forward(next)
            
            next=activation.ReLU( layer.output)
            layer.output=next
        self.outputLayr.forward(next)
        self.outputLayr.output=activation.softmax(self.outputLayr.output)
        
start = timeit.default_timer()

X=numpy.random.rand(128,3)
mynetwork=Network(3,5,"relu",2,5)
mynetwork.forward_All(X)

print("last layer\n\n\n",mynetwork.layers[-1].output)
print("output\n\n\n",mynetwork.outputLayr.output)


stop = timeit.default_timer()

print('Time: ', stop - start)  