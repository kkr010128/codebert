import itertools
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
a = b = 0
for i, list_ in enumerate(list(itertools.permutations([i for i in range(1, n + 1)]))):
    if tuple(p) == list_:
        a = i + 1
    if tuple(q) == list_:
        b = i + 1
print(abs(a - b))
