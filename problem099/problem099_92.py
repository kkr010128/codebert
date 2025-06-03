import math
N, K = map(int, input().split())

a = list(map(int, input().split()))

def cal(x):
    s = 0
    for aa in a:
        s += math.ceil(aa / x) - 1
    if s <= K: return True
    else: return False

l = 0
r = max(a)
while r - l > 1:
    mid = (l + r) // 2
    if cal(mid):
        r = mid
    else:
        l = mid
print(r)