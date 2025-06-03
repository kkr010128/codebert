s = input()

cnt_l = [0]*(len(s)+1)
cnt_r = [0]*(len(s)+1)

for i in range(1, len(s)+1):
    if s[i-1] == "<":
        cnt_l[i] = cnt_l[i-1] + 1
    else:
        cnt_l[i] = 0

for i in range(len(s)-1, -1, -1):
    if s[i] == ">":
        cnt_r[i] = cnt_r[i+1]+1
    else:
        cnt_r[i] = 0

ans = 0
for l, r in zip(cnt_l, cnt_r):
    ans += max(l, r)
print(ans)
