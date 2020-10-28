import copy
alist = [4,2,8,6,5]

blist1 = alist.copy()
blist2 = [*alist]
blist3 = copy.copy(alist)
blist4 = alist*1
blist5 = copy.deepcopy(alist)
blist6 = alist[:]

blist1[3] = 111
blist2[3] = 222
blist3[3] = 333
blist4[3] = 444
blist5[3] = 555
blist6[3] = 666



print(alist)