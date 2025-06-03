from itertools import combinations

n, a, q, ms, cache = int(input()), list(map(int, input().split())), input(), map(int, input().split()), {}

l = set(sum(t) for i in range(n) for t in combinations(a, i + 1))

for m in ms:
    print('yes' if m in l else 'no')