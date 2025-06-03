import itertools as it

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))

r = list(it.permutations(range(1, n+1)))

a = 0
b = 0
for i in range(len(r)):
    if r[i] == p:
        a = i
    if r[i] == q:
        b = i

print(abs(a-b))
