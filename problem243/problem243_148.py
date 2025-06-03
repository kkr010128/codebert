N = int(input())
s = [input().split() for _ in range(N)]
X = input()

for i in range(N):
    if X == s[i][0]:
        break

ans = 0
for j in range(i+1, N):
    ans += int(s[j][1])

print(ans)