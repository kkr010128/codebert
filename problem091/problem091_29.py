# coding: utf-8

num = int(input())
count = 0
str = input().split()
table = [int(i) for i in str]
#全探索
for j in range(num): #ループ1
    for k in range(j+1, num): #ループ2
        for l in range(k+1, num): #ループ3
            if table[j] != table[k] and table[k] != table[l] and table[j] != table[l]:
                len = table[j] + table[k] + table[l] #周の長さ
                ma = max(table[j], max(table[k], table[l])) #一番長い辺
                rest = len - ma #残りの2辺の合計
                if ma < rest: #最大の辺が残り2辺より小さければ三角形は成立する
                    count += 1
print(count)
