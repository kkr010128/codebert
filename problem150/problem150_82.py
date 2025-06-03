N, K = [int(_) for _ in input().split()]
A = [None] + [int(_) for _ in input().split()]
nowkaimin = [None] * (N + 1)
now = 1
kai = 0
nowkaimin[now] = kai
while True:
    now = A[now]
    kai += 1
    if kai == K:
        print(now)
        exit()
    if nowkaimin[now] is not None:
        break
    nowkaimin[now] = kai
#nowkaimin[now] to kai ga hitosii
#nowkaimin[now] + (kai - nowkaimin[now]) * Q + R
R = (K - nowkaimin[now]) % (kai - nowkaimin[now])
for i, v in enumerate(nowkaimin):
    if v == nowkaimin[now] + R:
        print(i)
        exit()
