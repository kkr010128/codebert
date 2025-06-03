n, m = map(int, input().split())

a = [[] for i in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0] * m
for i in range(m):
    b[i] = int(input())

for ai in a:
    cnt = 0
    for j, bj in enumerate(b):
        cnt += ai[j] * bj
    print(cnt)
