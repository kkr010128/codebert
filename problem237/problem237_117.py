N = int(input())

robo = []
for _ in range(N):
    X, L = map(int, input().split())
    robo.append([X-L, X+L])

robo = sorted(robo, key=lambda x:x[1])

last = robo[0][1]
cnt = 1
for r in robo[1:]:
    if r[0] >= last:
        cnt += 1
        last = r[1]

print(cnt)