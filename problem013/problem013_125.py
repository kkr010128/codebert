n = int(input())
R = (int(input()) for _ in range(n))
ret = -(10 ** 9)
mn = next(R)
for r in R:
    ret = max(ret, r - mn)
    mn = min(mn, r)
print(ret)