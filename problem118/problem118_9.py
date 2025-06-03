N = int(input())
ans = 0
for i in range(N):
    Y = int(N/(i+1))
    ans += Y * (Y + 1) * (i + 1) // 2
print(ans)