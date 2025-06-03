n, m = map(int, input().split())
h = [int(x) for x in input().split()]
cnt = [1] * n

for _ in range(m):
    a, b = map(int, input().split())
    if h[a-1] > h[b-1]:
        cnt[b-1] = 0
    elif h[a-1] < h[b-1]:
        cnt[a-1] = 0
    else:
        cnt[a-1] = 0
        cnt[b-1] = 0

print(cnt.count(1))