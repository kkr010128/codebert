n, k = map(int, input().split())
a = list(map(int, input().split()))
dist = [-1] * n

i = 0
dist[0] = 0
while True:
    nxt = a[i] - 1
    if dist[nxt] >= 0:
        if k > dist[nxt]:
            k -= dist[nxt]
            k %= dist[i] - dist[nxt] + 1
            k += dist[nxt]
        print(dist.index(k) + 1)
        break
    dist[nxt] = dist[i] + 1
    i = nxt