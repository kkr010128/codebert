n, k = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

ls = [-1] * n
now = 0
cnt = 0
path = []
while 1:
    if ls[now] != -1:
        b = ls[now]
        break
    ls[now] = cnt
    path.append(now)
    now = a[now]
    cnt += 1
loop = path[b:]
if k <= b:
    print(path[k] + 1)
else:
    print(loop[(k - b) % len(loop)] + 1)
