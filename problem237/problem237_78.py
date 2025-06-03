n = int(input())
x_list = []
l_list = []
for i in range(n):
    x, l = map(int, input().split())
    x_list.append(x)
    l_list.append((x - l, x + l))

l_list = sorted(l_list, key=lambda a:a[1])
# print(l_list)
t = l_list[0][1]
ans = 1
for i in range(1, n):
    s = l_list[i][0]
    if s < t:
        continue
    t = l_list[i][1]
    ans += 1

print(ans)