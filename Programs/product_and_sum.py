from itertools import combinations
import numpy
s,p,k=[int(i) for i in input().split()]
l=[i for i in range(1,s-1)]+[i for i in range(1,s-1)]
comb=combinations(l,k)
for i in list(comb):
  if sum(i)==s and numpy.prod(i)==p:
    print(*i)
    break
else:
  print('NO')