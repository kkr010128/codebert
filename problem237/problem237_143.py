N = int(input())
R = []
for _ in range(N):
    x, L = map(int, input().split())
    R.append([x - L, x + L])

R.sort(key=lambda x: x[1])

ans = 1
for i in range(N):
    if (i == 0):
        first = R[0][1]
        continue

    if first <= R[i][0]:
        first = R[i][1]
        ans += 1

print(ans)
