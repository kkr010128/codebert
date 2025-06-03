#インプットdataの格納
n, k = map(int, input().split())
n_list = list()
for i in range(n):
    n_list.append(int(input()))

#data処理
left = 0
right = 100000*10000
while (right - left) > 1:
    mid = (left + right) // 2

    i = 0
    for j in range(k):
        weight = 0
        while i < n:
            if (weight + n_list[i]) > mid:
                break
            else:
                weight += n_list[i]
                i += 1

    if i >= n:
        right = mid
    else:
        left = mid
        
#結果表示
print(right)

