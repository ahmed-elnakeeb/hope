import cProfile
import random
from numpy.random import default_rng
import numpy
import timeit


class Network:
    def __init__(self,inputs=2,outputs=2,layers_number=2,layer_Size=10):
        super().__init__()
        self._inputs=inputs
        self._outputs=outputs
        self._layers_number=layers_number+2
        self._laiersize=layer_Size
        self.input_Layer=numpy.zeros(inputs)
        self.hiddennlyers=numpy.random.rand(layers_number,layer_Size)


        self.layers=[numpy.zeros(inputs),*self.hiddennlyers,numpy.random.rand(outputs)]
        self.setweights()


    def do(self,input:list):
        if len(input)==self._inputs:
            self.layers[0]=input
        else:
            sys.exit()
        for i in range(len(self.layers)-1):

            print("weight:",self.weights[i],"\n\n\n:layer",self.layers[i],"\n\n\nnextlayer:", self.layers[i+1],"\n\n\noutput:")
            try:
                output=numpy.dot(self.weights[i],numpy.array(self.layers[i]))

            except:
                x,y=numpy.array(self.layers[i]).shape

                output=numpy.dot(self.weights[i],numpy.array(self.layers[i].reshape(y*x)))

            print("\n\n\noutput:",output)

            self.layers[i+1]=output+ self.layers[i+1]
            print("##################################################")
        return(output)
            



    def dispaly(self):
        print("input :",self.input_Layer,"\noutput :",self.layers[-1],"\nfirstlayer:",self.layers[0],"\nweights:",str(self.weights))

    def setweights(self):
        self.weights=[numpy.random.rand(self._laiersize,self._inputs)]
        for i in range(1,self._layers_number-2):
            self.weights.append([numpy.random.rand(self._laiersize,self._laiersize)])
        self.weights.append(numpy.random.rand(self._outputs,self._laiersize))







import timeit

start = timeit.default_timer()
mynetwork=Network(inputs=3,outputs=5,layer_Size=100,layers_number=10)

print(mynetwork.do([1,2,3]))

stop = timeit.default_timer()

print('Time: ', stop - start)  






# rng = default_rng()
# self.nurals = rng.standard_normal(size)
        


# input_Layer=[0,0,0]

# hiden_layers_number=[[2,1,5,3],[2,3,2]]

# output_Layer=[6,2]



# weights1 =[ [1,2,3],
#             [1,1,4],
#             [0,1,5],
#             [2,1,2]]

# weights2 =[ [0,0,0,1],
#             [1,7,0,2],
#             [2,5,9,0]]

# weights3 =[ [1,0,3],
#             [5,5,5]]
