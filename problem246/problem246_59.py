from itertools import *
A = list(permutations(range(1,1+int(input()))))
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
print(abs(A.index(P)-A.index(Q)))