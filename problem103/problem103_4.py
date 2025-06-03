# まず底をみつけてそのあと山で売るを繰り返す
n = int(input())
arr = list(map(int, input().split()))
arr2 = []
cur = arr[0] if arr[0] < arr[1] else 10**10
f = 1
for i in range(1, n):
    if f == 1:
        # print("底値を求める")
        if cur < arr[i]:
            arr2.append(cur)
            f *= -1
    else:
        # print("天井を求める")
        if cur > arr[i]:
            arr2.append(cur)
            f *= -1
    cur = arr[i]
if f == -1:
    arr2.append(cur)
ans = 1000
stock = 0
for i, a in enumerate(arr2):
    if i % 2 == 0:
        # 買いまくる
        stock = ans // a
        ans %= a
    else:
        # うりまくる
        ans += stock * a
        stock = 0
print(ans)