H,W,N = map(int, open(0).read().split())

ans = 0
while N > 0:
    A = max(H, W)
    tmp = N // A
    N = N % A
    if tmp == 0 and N:
        N = 0
        ans += 1
        break
    if H == A:
        W -= tmp
    else:
        H -= tmp
    ans += tmp

print(ans)