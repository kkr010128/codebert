s = input()
t = input()
sl = len(s)
tl = len(t)
ans = 1001

for i in range(sl-tl+1):
    cnt = 0
    for sv, tv in zip(s[i:i+tl], t):
        if sv != tv:
            cnt += 1
    ans = min(cnt, ans)

print(ans)
