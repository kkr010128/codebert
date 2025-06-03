H, W, K, *S = open(0).read().split()
H, W = int(H), int(W)

c = 0
n = 0
for s in S:
    l, r = -1, s.find("#")
    n += 1
    if r == -1:
        continue
    T = []
    while r != -1:
        c += 1
        T += [c] * (r - l)
        l, r = r, s.find("#", r + 1)
    T += [c] * (W - l - 1)
    for i in range(n):
        print(*T)
    n = 0

for i in range(n):
    print(*T)