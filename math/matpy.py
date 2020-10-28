from sympy import symbols, solve
class part:
    sign=""
    value=""
    def __init__(self,p:str):
        super().__init__()
    def _validate(self):
        pass

class equation:
    lhs=""
    rhs=""
    myvars={}
    
    def __init__(self,lhs:str,rhs:str):
        super().__init__()
        self.lhs=lhs
        self.rhs=rhs
        self._find_vars()
        self.trysolve()
    def _find_vars(self):
        for i in self.rhs:
            if i.isalpha():
                self.myvars[i]=""
        ########################
        for i in self.lhs:
            if i.isalpha():
                self.myvars[i]=""

    def trysolve(self):
        if len(self.myvars)==1:
            pass
        else:
            return 
        print("try")
        try:
            self.lhs=str(eval(self.lhs))
        except :
            pass
        ###################
        try:
            self.rhs=str(eval(self.rhs))
        except :
            pass

    def info(self):
        return [self.lhs,self.rhs,self.myvars]

e=equation("1**2","b*b")
print(e.info())