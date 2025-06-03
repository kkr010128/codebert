##############################################
N = int(input())
X = list(map(int, input().split()))

ans = float('inf')

for i in range(min(X), max(X)+1):
    cost = 0
    for x in X:
        cost += (x - i) ** 2

    ans = min(ans, cost)

print(ans)