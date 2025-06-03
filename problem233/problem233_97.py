N = int(input())
P = list(map(int, input().split()))

min = P[0]
ans = 0

for i in range(N):
    if i == 0:
        ans += 1
    elif min > P[i]:
        ans += 1
        min = P[i]

print(ans)