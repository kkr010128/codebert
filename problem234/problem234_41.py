N = int(input())
top_bottom = [[0]*10 for _ in range(10)]
for i in range(1, N + 1):
    s = str(i)
    top_bottom[int(s[0])][int(s[-1])] += 1
ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += top_bottom[i][j] * top_bottom[j][i]
print(ans)
