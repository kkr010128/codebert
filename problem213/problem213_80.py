N = int(input())
X = list(map(int, input().split()))

INF = 10**6 + 1
mintotal = INF
for p in range(1, 101):
    total = 0
    for x in X:
        total += (x-p)**2
    mintotal = min(mintotal, total)
print(mintotal)