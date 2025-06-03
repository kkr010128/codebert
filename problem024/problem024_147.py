import sys

def check(p):
    s = w[0]
    track = 1
    for i in range(1, n):
        if s + w[i] <= p:
            s += w[i]
        else:
            track += 1
            if track > k: return False
            s = w[i]
    return True

n, k = map(int, sys.stdin.readline().strip().split())
w = []
for i in range(n):
    w.append(int(sys.stdin.readline()))

L = max(w)
if check(L):
    print(L)
else:
    R = sum(w)
    assert check(R)

    while L + 1 < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M

    print(R)