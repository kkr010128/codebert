n = int(input())

min_price = int(input())
max_diff = -1e9

for _ in range(n - 1):
    p = int(input())
    max_diff = max(p - min_price, max_diff)
    min_price = min(p, min_price)

print(max_diff)