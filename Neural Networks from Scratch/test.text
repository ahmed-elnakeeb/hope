import numpy

inputs = numpy.random.rand(10)

w = numpy.random.rand(100,10)

bias=numpy.random.rand(100)

# output=[inputs[0]*w[0,0]+inputs[1]*w[0,1]+inputs[2]*w[0,2]+inputs[3]*w[0,3] +bias[0],
# inputs[0]*w[1,0]+inputs[1]*w[1,1]+inputs[2]*w[1,2]+inputs[3]*w[1,3] +bias[1],
# inputs[0]*w[2,0]+inputs[1]*w[2,1]+inputs[2]*w[2,2]+inputs[3]*w[2,3] +bias[2]]
# print(max( output))
# print( output)

output=numpy.dot(w,inputs)+bias
print(max(output),len(output))








output=[]

for i in range(len(w)):
    sum=0
    for n_input in range(len(w[0])):
        sum+=inputs[n_input]*w[i,n_input]
    sum+=bias[i]
    output.append(sum)

# print(max( output))
print(max(output),len(output))
