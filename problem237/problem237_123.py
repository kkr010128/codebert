n = int(input())
x_list = []
for _ in range(n):
    x, l = map(int, input().split())
    x_list.append((x + l, x - l))
x_list.sort()
ans = 0
for i in range(n):
    x_max, x_min = x_list[i]
    if i == 0:
        t = x_max
        continue
    if x_min < t:
        ans += 1
        continue
    t = x_max
print(n - ans)