n = int(input())

# 連続する場合は無視できるので圧縮
tmp = list(map(int, input().split()))
arr = [tmp[0]]
for i in range(1, n):
    if arr[-1] != tmp[i]:
        arr.append(tmp[i])

# 株価が上がる前に全力で買って、上がったら全力で売る。を貪欲にやる
money, stock = 1000, 0
for i in range(1, len(arr)):
    if arr[i - 1] < arr[i]:
        # 全力買い
        buy, money = divmod(money, arr[i - 1])
        stock += buy
        # 全力売り
        money += stock * arr[i]
        stock = 0

print(money)