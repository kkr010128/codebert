n, d = map(int, input().split(" "))
p = []
ans = 0
for i in range(n):
    p.append(list(map(int, input().split(" "))))

for i, [x, y] in enumerate(p):
    if(x > d or y > d):
        continue
    if(x**2 + y**2 <= d**2):
        ans += 1


print(ans)