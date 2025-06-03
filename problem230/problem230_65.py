import bisect
import math
N, D, A = map(int, input().split())
cusum = [0] * (N+1)
X = []
XH =[]
for i in range(N):
    xi, hi = map(int, input().split())
    X += [xi]
    XH += [(xi, hi)]
X = sorted(X)
XH = sorted(XH)
cusumD = 0
ans = 0
for i, (xi, hi) in enumerate(XH):
    cusumD -= cusum[i]
    hi = max(0, hi-cusumD)
    r = bisect.bisect_right(X, xi+2*D)
    b = int(math.ceil(hi/A))
    d = b * A
    ans += b
    cusumD += d
    cusum[r] += d
    
print(ans)
