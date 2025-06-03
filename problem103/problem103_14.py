n = int(input())
a = list(map(int, input().split()))

money = 1000
mount = 0

f = -1
pre = a[0]
for i in range(1, len(a)):
    if f < 0:
        if a[i] <= pre:
            pre = a[i]
            continue
        mount += money // pre
        money %= pre
        f *= -1
    else:
        if a[i] >= pre:
            pre = a[i]
            continue
        money += mount * pre
        mount = 0
        f *= -1

    pre = a[i]

money += mount * a[-1]
print(money)
