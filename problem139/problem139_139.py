h1, m1, h2, m2, k = map(int, input().split())
if h1 > h2:
    h1 += 24

act_time = (h2 * 60 + m2) - (h1 * 60 + m1)
ans = act_time - k
print(ans)