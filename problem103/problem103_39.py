n = int(input())
a = list(map(int, input().split()))
x = []
flag = True
for i in reversed(range(n)):
    if i == 0:
        if not flag:
            x.append(a[i])
        break
    flag2 = flag
    if flag:
        if a[i - 1] < a[i]:
            x.append(a[i])
            flag2 = not flag2
    else:
        if a[i - 1] > a[i]:
            x.append(a[i])
            flag2 = not flag2
    flag = flag2
x = x[::-1]
m = len(x)
if m % 2 == 1:
    x = x[1:]
# print("x =", x)
cur_money = 1000
cur_stock = 0
for i in range(m):
    if i % 2 == 0:
        cur_stock += cur_money // x[i]
        cur_money %= x[i]
    else:
        cur_money += x[i] * cur_stock
        cur_stock = 0
print(cur_money)