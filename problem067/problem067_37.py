taro = 0
hana = 0
n = int(input())
for _ in range(n):
    taro_s, hana_s = map(str, input().split())
    if taro_s > hana_s:
        taro += 3
    elif hana_s > taro_s:
        hana += 3
    else:
        taro += 1
        hana += 1
print(taro, hana)

