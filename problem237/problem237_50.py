N = int(input())

f = []
for i in range(N):
    x, l = map(int, input().split())
    f.append([x - l, x + l])
f.sort(key=lambda x: x[1])

t = f[0][1]
ans = 1
for i in range(1, N):
    if f[i][0] < t:
        continue
    ans += 1
    t = f[i][1]
print(ans)
