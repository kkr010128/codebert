import itertools
N = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))

lis = list(itertools.permutations(range(1,N+1)))
a = lis.index(P)+1
b = lis.index(Q)+1
ans = abs(a-b)
print(ans)