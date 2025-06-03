k, n = map(int, input().split())
a = list(map(int, input().split()))
diff = []

for i in range(len(a)):
    if (i == len(a) - 1):
        distance = a[0] + (k - a[-1])

    else:
        tar2 = a[i + 1]
        tar1 = a[i]
        distance = tar2 - tar1

    diff.append(distance)

# スタート位置を見つける
index = diff.index(max(diff))
ans = sum(diff) - max(diff)

print(ans)
# print(index)
# > 2なので、15~5は避ける。
# if (index == len(diff)):
