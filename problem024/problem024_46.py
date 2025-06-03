N, K = map(int, input().split())
W = [int(input()) for w in range(N)]

def check(p):
    i = 0
    for _ in range(K):
        s = 0
        while s + W[i] <= p:
            s += W[i]
            i += 1
            if i == N:
                return N
    return i

left = 0
right = 100000 * 10000
mid = 0
while 1 < right - left:
    mid = (left + right) / 2
    v = check(mid)
    if v >= N:
        right = mid
    else:
        left = mid

print(int(right))
