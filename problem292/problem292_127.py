from itertools import *
N = int(input())
D = list(map(int,input().split()))
print(sum(x*y for x,y in combinations(D,2)))