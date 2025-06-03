N = int(input())
pos = []
for _ in range(N):
    x, l = map(int,input().split())
    pos.append((x+l, x-l))

pos.sort()

ans = 0
cur = float('-inf')
for i in range(N):
    if cur <= pos[i][1]:
        ans += 1
        cur = pos[i][0]

print(ans)