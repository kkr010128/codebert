
count = 0

n, d = map(int, input().split())
for _ in range(n):
    l, m = map(int, input().split())
    z = (l ** 2 + m ** 2) ** 0.5
    if z <= d:
        count += 1


print(count)
