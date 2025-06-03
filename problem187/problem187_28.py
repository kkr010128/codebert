from collections import Counter
from itertools import combinations

N, X, Y = map(int, input().split(' '))

c = Counter()
for i, j in combinations(range(1, N + 1), r=2):
    c[min(j - i, abs(X - i) + 1 + abs(j - Y))] += 1

for n in range(1, N):
    print(c[n])
