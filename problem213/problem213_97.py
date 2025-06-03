N = int(input())
Xs = list(map(int, input().split()))

ans = 10**10
for P in range(0, 102):
    cost = 0
    for X in Xs:
        cost += (X-P)**2
    ans = min(ans, cost)

print(ans)
