import itertools
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
t,h = 0,0
a = list(itertools.permutations(range(1,n+1)))
for i,c in enumerate(a):
    if p == c:
        t = i
    if q == c:
        h = i
print(abs(t-h))