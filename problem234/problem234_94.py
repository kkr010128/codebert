N = int(input())
c = [[0]*10 for _ in range(10)]

for i in range(1, N+1):
    end = i%10
    head = int(str(i)[0])
    c[head][end] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j]*c[j][i]

print(ans)
