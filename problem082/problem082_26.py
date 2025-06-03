s = input()
t = input()
s_len = len(s)
t_len = len(t)

ans = 99999

for i in range(-~s_len-t_len):
    cnt = 0
    for j in range(t_len):
        if s[i+j] != t[j]:
            cnt += 1
    ans = min(ans, cnt)

print(ans)