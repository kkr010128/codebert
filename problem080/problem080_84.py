n = int(input())
s = []

for i in range(n):
    x, y = map(int, input().split())
    s.append([x + y, x - y])

t = sorted(s)
u = sorted(s, key=lambda x: x[1])
res = 0

tmp1 = t[-1][0] - t[0][0]
tmp2 = u[-1][1] - u[0][1]

print(max(tmp1, tmp2))
