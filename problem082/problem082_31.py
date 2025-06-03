s = input()
t = input()

ans = 1e+9

for si in range(len(s)):
    if si + len(t) > len(s):
        continue
    cnt = 0
    for ti in range(len(t)):
        if s[si+ti] != t[ti]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)