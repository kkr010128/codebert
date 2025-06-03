h1, m1, h2, m2, k = map(int, input().split())
st = h1 * 60 + m1
ed = h2 * 60 + m2
ans = ed - st - k
if ans < 0:
    ans = 0
print(ans)
