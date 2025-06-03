N = int(input())

cnt = [[0 for i in range(10)] for j in range(10)]

for i in range(1, N+1):
    i_str = str(i)
    cnt[int(i_str[0])][int(i_str[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += cnt[i][j] * cnt[j][i]

print(ans)