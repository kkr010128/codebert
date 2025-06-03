r, c = map(int, input().split())

x = []
for _ in range(r):
    x.append(list(map(int, input().split())))

c_line_sum = []
for i in range(c): # 列の総和の計算
    t = []
    for j in range(r):
        t.append(x[j][i])
    c_line_sum.append(sum(t))

for i in range(r): # 行の総和の計算
    x[i].append(sum(x[i]))

c_line_sum.append(sum(c_line_sum))
x.append(c_line_sum)

for m in x:
    print(*m)
