from itertools import *
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
dic = dict()
i = 0
for a in permutations(range(1,N+1),N):
    dic[a] = i
    i += 1
print(abs(dic[P]-dic[Q]))