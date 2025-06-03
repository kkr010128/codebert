n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]

for i, ai in enumerate(a):
    cnt = 0
    for j, bj in enumerate(b):
       cnt += ai[j] * bj
    print(cnt)
