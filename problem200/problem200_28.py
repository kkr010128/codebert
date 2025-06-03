A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

min_price = min(a) + min(b)
for _ in range(M):
    x, y, c = map(int, input().split())
    discount_price = a[x-1] + b[y-1] - c
    if min_price > discount_price:
        min_price = discount_price
        
print(min_price)
