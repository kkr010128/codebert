import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))


for i, l in enumerate(itertools.permutations(range(1, n + 1))):
    if list(l) == p:
        a = i
    if list(l) == q:
        b = i
print(abs(a - b))
