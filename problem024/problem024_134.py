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

n, k = [int(i) for i in input().split()]
w = []
for i in range(n):
    w.append(int(input()))
L = max(w)
R = sum(w)

if check(L):
    print(L)
else:
    while L + 1 < R:
        M = (L + R) // 2
        if check(M):
            R = M
        else:
            L = M
    print(R)