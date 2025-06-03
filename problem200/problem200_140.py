a, b, m = list(map(int, input().split()))
refrigerator_list = list(map(int, input().split()))
microwave_list = list(map(int, input().split()))
coupon_list = list()
for _ in range(m):
    coupon_list.append(list(map(int, input().split())))

ans = min(refrigerator_list) + min(microwave_list)
for coupon in coupon_list:
    ans = min(refrigerator_list[coupon[0] - 1] + microwave_list[coupon[1] - 1] - coupon[2], ans)

print(ans)
