def check_p(p):
    global k, ws
    ct, nt = 0, 1
    for w in ws:
        if ct + w <= p:
            ct += w
        else:
            nt += 1
            if nt > k:
                return False
            ct = w
    return True


n, k = map(int, input().split())

ws = [int(input()) for _ in range(n)]
l, r, p = max(ws), sum(ws), 0

while l < r:
    p = (l + r) // 2
    if check_p(p):
        r = p
    else:
        l = p = p + 1

print(p)