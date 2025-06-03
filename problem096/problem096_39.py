n,d = map(int, input().split())
z = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in z:
    distance = i[0]*i[0] + i[1]*i[1]
    if distance <= d**2:
        ans += 1

print(ans)
