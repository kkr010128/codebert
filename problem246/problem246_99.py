import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
c = [i for i in range(1,n+1)]
v = list(itertools.permutations(c,n))
a = v.index(p)
b = v.index(q)
print(abs(a-b))