a, b, c, k = (int(i) for i in input().split())
res = 1 * min(a, k) + 0 * min(b, max(0, k - a)) + -1 * min(c, max(0, k - a - b))
print(res)
