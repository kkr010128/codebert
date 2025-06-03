n = int(input())
a = list(map(int, input().split()))

left = a[0]
right = a[-1]
center = 0
sum_a = sum(a)
flg = False
for i in range(1, n-1):
    if left + a[i] > sum_a/2 and flg is False:
        flg = True
        center = a[i]
        right -= a[i]
    elif left + a[i] == sum_a / 2:
        print(0)
        exit()
    if flg is False:
        left += a[i]
    else:
        right += a[i]

print(abs(min(left+center-right, right+center-left)))
