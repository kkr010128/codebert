A, B, M = map(int, input().split())
As = list(map(int, input().split()))
Bs = list(map(int, input().split()))
coupons = []
for _ in range(M):
    x, y, c = map(int, input().split())
    coupons.append((x, y, c))

price_min = min(As) + min(Bs)
coupon_min = min([As[x - 1] + Bs[y - 1] - c for (x, y, c) in coupons])

print(min((price_min, coupon_min)))
