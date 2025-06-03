n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(m):
    b.append(int(input()))

for i, ai in enumerate(a):
    cnt = 0
    for j, bj in enumerate(b):
       cnt += ai[j] * bj
    print(cnt)
