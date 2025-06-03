n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse = True)
cost = max([a[i] * f[i] for i in range(n)])
cost2 = 0
while True:
    cost3 = (cost + cost2) // 2
    count = 0
    for i in range(n):
        count += max((a[i] * f[i] - cost3 - 1) // f[i] + 1, 0)
    if count <= k:
        cost = cost3
    else:
        cost2 = cost3 + 1
    if cost == cost2:
        break
print(cost)