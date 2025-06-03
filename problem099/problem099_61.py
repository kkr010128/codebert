import math

N, K = map(int,input().split())
A = list(map(int, input().split()))

l, r = 0, max(A)
while r - l > 1:
    x = (l + r) // 2
    cnt = 0
    for a in A:
        n = math.ceil(a / x)
        # n = (a + x - 1) // x
        cnt += n - 1
    if cnt > K:
        l = x 
    else:
        r = x

print(r)
