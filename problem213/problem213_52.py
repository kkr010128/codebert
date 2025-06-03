N = int(input())
X = [int(x) for x in input().split()]

G = int(sum(X)/N + 0.5)

ans = sum((x-G)**2 for x in X)

print(ans)