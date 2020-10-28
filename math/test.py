# numps={"a":5,"b":6}
# print(eval("numps['a']+numps['b']"))
from sympy import Symbol, cos, Eq, solve
x= Symbol('x')
eq1 = Eq(x**2 -5*x + 5,-1)


sol = solve(eq1,dict=True,set=True)
print(*sol)