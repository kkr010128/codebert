n , m , x = map(int, input().split())
a = list(list(map(int, input().split())) for _ in range(n))

c = []
for i in range(n):
    c.append(a[i][0])
    a[i].pop(0)

ans = 1000000000

for i in range(1 << n):
    score = [0] * m
    tmp = 0
    for j in range(n):
        if (i >> j) % 2 == 1:
            tmp += c[j]
            for k in range(m):
                score[k] += a[j][k]

    check = True
    for l in range (m):
        if score[l] < x:
            check = False

    if check:
        ans = min(ans , tmp)

if(ans == 1000000000):
    print(-1)
else:
    print(ans)
