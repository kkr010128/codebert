s = input()
s_l = [0] * (len(s) + 1)
s_r = [0] * (len(s) + 1)
for i in range(len(s)):
    if s[i] == '<':
        s_l[i + 1] = s_l[i] + 1
for i in range(len(s)):
    if s[- i - 1] == '>':
        s_r[- i - 2] = s_r[- i - 1] + 1
        
ans = 0
for i, j in zip(s_l, s_r):
    ans += max(i, j)
print(ans)