import re
from itertools import product
import itertools

q1 = int(input())
q2 = input()
q3 = int(input())
q4 = input()

S = re.split(r' ',q2)
S=list(map(int, S))

T = re.split(r' ',q4)
T=list(map(int, T))

S_len = len(S)
T_len = len(T)

array = []
for j in range(q1+1):
    x = list(itertools.combinations(S, j))
    for k in range(len(x)):
        y = sum(x[k])
        array.append(y)

for i in range(T_len):
    if(T[i] in array):
        print("yes")
    else:
        print("no")
