n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

plus = []
minus = []
for i in a:
    if i >= 0: plus.append(i)
    if i < 0: minus.append(-i)
plus.sort(reverse=True)
minus.sort(reverse=True)

ans = 1
if k == n:
    for x in a:
        ans = (ans * x) % mod
elif n == len(plus):
    for x in plus[:k]:
        ans = (ans * x) % mod
elif n == len(minus):
    if k % 2 == 1:
        ans = -1
        minus.sort()
    for x in minus[:k]:
        ans = (ans * x) % mod
else:
    i, j = 0, 0
    if k % 2 == 1:
        ans = plus[0]
        i += 1
    while i + j != k:
        x_p = plus[i] * plus[i + 1] if i < len(plus) - 1 else 0
        x_m = minus[j] * minus[j + 1] if j < len(minus) - 1 else 0
        if x_p > x_m:
            ans = (ans * x_p) % mod
            i += 2
        else:
            ans = (ans * x_m) % mod
            j += 2
print(ans)