import numpy as np
import matplotlib.pyplot as plt
class linepint:
    def __init__(self,x:float,y:float,m:float,c:float):
        self.x=float(x)
        self.y=float(y)
        self.c=float(c)
        self.m=float(m)
class line:
    def __init__(self,m:float,c:float):
        self.c=float(c)
        self.m=float(m)
class point:
    def __init__(self,x:float,y:float):
        self.x=float(x)
        self.y=float(y)
class tools:
    @staticmethod
    def get_unknown(*,x=None,y=None,m=None,c=None):
        if x==None and y!=None and m!=None and c!=None:
            x=(y-c)/m
            return tools.printeq(linepint(x,y,m,c))
        elif y==None and x !=None and m !=None and c !=None:
            y=m*x+c
            return tools.printeq(linepint(x,y,m,c))
        elif m==None and x !=None and y !=None and c !=None:
            m=(y-c)/x
            return tools.printeq(linepint(x,y,m,c))
        elif c==None and x !=None and y !=None and m !=None:
            c=y-m*x
            return tools.printeq(linepint(x,y,m,c))
    @staticmethod
    def printeq(eq:linepint):
        return ("x= "+str(eq.x)+"\ny= "+str(eq.y)+"\nc= "+str(eq.c)+"\nm= "+str(eq.m))
    


        
"""
data={
    (0,0),(1,2),(2,1),(3,3),(4,5),(5,4),(6,6),(7,8),(8,7),(9,9),(10,10)
}
data2={
0:0,1:2,2:1,3:3,4:5,5:4,6:6,7:8,8:7,9:9,10:10
}
exact
f(x)=y=mx+c
x=input
y=output
f=function that draives x to y
m=slope
c=y value for x=0

aproxmate
h(x)=ty+z
where error is minimum 
error(t,z)=1/2m (  sum{f-h}^2  )

"""



        
c=tools.get_unknown(m=1,c=2,y=None,x=-2)

print(c)

p=point(1,2)
V = np.array([[100,0],[0,100],[-100,0],[0,-100]])
origin = [0], [0] # origin point
plt.quiver(*origin, V[0][0], V[0][1],scale=1)
plt.quiver(*origin, V[1][0], V[1][1],scale=1)
plt.quiver(*origin, V[2][0], V[2][1],scale=1)
plt.quiver(*origin, V[3][0], V[3][1],scale=1)
plt.scatter(1,1)
plt.scatter(2,2)
plt.scatter(0,0)
plt.scatter(p.x,p.y)
plt.grid(b=True, which='major') #<-- plot grid lines
plt.show()
