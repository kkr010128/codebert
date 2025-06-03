from math import floor

def solve(X, D, lb, ub):
    # min abs(X + t * D) (lb <= t <= ub) (lb, ub, t are int)
    ts = [
        lb,
        ub,
        max(min(floor(-X / D), ub), lb),
        max(min(floor(-X / D) + 1, ub), lb),
    ]   
    return min([abs(X + t * D) for t in ts])

X, K, D = map(int, input().split())

y1 = X - K * D
y2 = X + K * D
if (y1 > 0 and y2 > 0) or (y1 < 0 and y2 < 0): # same sign
    print(min(abs(y1), abs(y2)))
else:
    if K % 2 == 0:
        ans = solve(X, D * 2, -(K // 2), +(K // 2))
    else:
        ans1 = solve(X + D, D * 2, -((K + 1) // 2), +((K - 1)) // 2)
        ans2 = solve(X - D, D * 2, -((K - 1) // 2), +((K + 1)) // 2)
        ans = min(ans1, ans2)
    print(ans)

