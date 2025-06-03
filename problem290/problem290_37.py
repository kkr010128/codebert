N, K = map(int, input().split())
*A, = map(int, input().split())
*F, = map(int, input().split())
A, F = sorted(A), sorted(F, reverse=True)

def cond(x):
    k = 0
    for a, f in zip(A, F): k += max(a - (x // f), 0)
    return True if k <= K else False 

MIN = -1
MAX = 10**12 + 1
left, right = MIN, MAX # search range
while right - left > 1:
    mid = (left + right) // 2
    if cond(mid): right = mid
    else: left = mid
print(right)