word1, word2 = "hullaballoo","cacophony"

set_word1 = set("hullaballoo")
set_word2 = set("cacophony")

s1=set()
s2=set()


i=[1,2,3]
i2=[1,2]

# print(set_word1.union(word1))
# print(set_word1)
# print(set_word1.difference(word1))
# print(set_word1.intersection(word1))
# print(set_word1)


def setanddontlenmerepeat(word:str):
    x=len(word)
    a,b=[],[]
    if x<2:
        print(word)
        return set(word)
    elif x==2:
        a=word[0]
        b=word[1]
    else:
        a=word[0:int(x/2)]
        b=word[int(x/2):]
    seta1=set(a)
    seta2=set(a)
    setb1=set(b)
    seta2=set(b)

    c=seta1.difference(setb1)
    c2=[]
    d2=[]
    try:
        c2=(a).remove(*list(c))
    except :
        pass
    d=setb1.difference(seta1)
    try:
        d2=(a).remove(*list(d))
    except :
        pass
    e=c.union(d)
    try:
        c2=set(c2)
    except:
        c2=set()
    
    try:
        d2=set(d2)
    except:
        d2=set()

    set(e).difference(c2.union(d2))




    print (e)

# print(setanddontlenmerepeat("1"))
setanddontlenmerepeat("12312344")