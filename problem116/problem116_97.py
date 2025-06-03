s, t = open(0).read().split()
ans = 0
for ch_s, ch_t in zip(s, t):
    if ch_s != ch_t:
        ans += 1
print(ans)