n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]

def check(P):
    s, cnt = 0, 1
    for i in range(n):
        if w[i] > P:
            return False
        if s + w[i] <= P:
            s += w[i]
        else:
            s = w[i]
            cnt += 1
    return cnt <= k

l, r = 0, 10000 * n
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        r = m
    else:
        l = m

print(r)