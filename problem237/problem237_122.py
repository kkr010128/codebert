N, *XL = map(int, open(0).read().split())
XL = sorted((x + l, x - l) for x, l in zip(*[iter(XL)] * 2))
curr = -float("inf")
ans = 0
for right, left in XL:
    if left >= curr:
        curr = right
        ans += 1
print(ans)

