import itertools

N = int(input())
d = list(map(int, input().split()))

combi = list(itertools.combinations(range(N), 2))
sumD = 0
for x in combi:
    sumD += d[x[0]] * d[x[1]]

print(sumD)
