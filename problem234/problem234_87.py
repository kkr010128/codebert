n = int(input())
lst = [[0 for j in range(10)] for i in range(10)]

for i in range(1, n+1):
    num = str(i)
    lst[int(num[0])][int(num[-1])] += 1

cnt = 0
for i in range(10):
    for j in range(i, 10):
        if i == j:
            cnt += lst[i][j] * lst[j][i]
        else:
            cnt += lst[i][j] * lst[j][i] * 2
print(cnt)