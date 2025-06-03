s = input()
t = input()
len_s = len(s)
len_t = len(t)
ans = len_t
for i in range(len_s - len_t + 1):
    tmp_cnt = 0
    tmp_s = s[i:i + len_t]
    for c1, c2 in zip(tmp_s, t):
        if c1 != c2:
            tmp_cnt += 1
    ans = min(ans, tmp_cnt)
print(ans)