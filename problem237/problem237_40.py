(N,), *XL = [list(map(int, s.split())) for s in open(0)]
XL.sort(key=lambda x: x[0] + x[1])
curr = -float("inf")
ans = 0
for x, l in XL:
    if x - l >= curr:
        curr = x + l
        ans += 1
print(ans)
