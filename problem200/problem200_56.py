a, b, m = map(int, input().split())
lsa = list(map(int, input().split()))
lsb = list(map(int, input().split()))
cost = min(lsa) + min(lsb)
for i in range(m):
    x, y, c = map(int, input().split())
    cost2 = lsa[x - 1] + lsb[y - 1] - c
    if cost2 < cost:
        cost = cost2

print(cost)
