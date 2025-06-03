a, b, m = map(int, input().split())
a_price = list(map(int, input().split()))
b_price = list(map(int, input().split()))
coupon = []
for _ in range(m):
    coupon.append(list(map(int, input().split())))

a_copy = a_price.copy()
a_copy.sort()
b_copy = b_price.copy()
b_copy.sort()
a_min = a_copy[0]
b_min = b_copy[0]
min = a_min + b_min
totals = [min]
for list in coupon:
    tmp = a_price[list[0] - 1] + b_price[list[1] - 1] - list[2]
    totals.append(tmp)

totals.sort()
ans = totals[0]

print(ans)
