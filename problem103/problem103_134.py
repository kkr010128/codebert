n = int(input())
al = list(map(int,input().split()))

kabu = 0
money = 1000
for i in range(n-1):
    if al[i] < al[i+1]:
        # 全部売る
        money += kabu * al[i]
        kabu = 0
        # 全部買う
        kabu += money // al[i]
        money = money % al[i]
    else:
        # 全部売る
        money += kabu * al[i]
        kabu = 0

print(money+ kabu*al[-1])