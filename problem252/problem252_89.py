from itertools import accumulate
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
lb = 0
ub = 2*10**5+1
while ub - lb > 1:
    m = (lb + ub) // 2
    cnt = 0
    s, t = 0, N-1
    while t >= 0:
        while s < N and A[s] + A[t] >= m:
            s += 1
        cnt += s
        t -= 1

    if cnt >= M:
        lb = m
    else:
        ub = m

accum = list(accumulate([0] + A))
ans = 0
cnt = 0
s, t = 0, N-1
while t >= 0:
    while s < N and A[s] + A[t] >= lb:
        s += 1
    ans += accum[s] + s * A[t]
    cnt += s
    t -= 1
print(ans - (cnt-M) * lb)
