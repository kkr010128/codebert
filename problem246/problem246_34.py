import itertools

n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
d = list(itertools.permutations(range(1, n + 1)))
d.sort()

a = -1
b = -1
for i in range(len(d)):
    if d[i] == p:
        a = i
    if d[i] == q:
        b = i
print(abs(a - b))