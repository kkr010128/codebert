n = int(input())
line = []
for _ in range(n):
    x, l = map(int, input().split())
    s, g = x-l, x+l
    line.append([g, s])

line.sort()
ans = 1
now_g = line[0][0]

for g, s in line[1:]:
    if now_g <= s:
        ans += 1
        now_g = g

print(ans)
