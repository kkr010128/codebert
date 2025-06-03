import collections

N=int(input())
P=[input() for i in range(N)]
c=collections.Counter(P)
print(len(c))