s = list(input())
n = len(s)
m = n//2
s_f = []
s_l = []
for i in range(m):
    s_f.append(s[i])
for i in range(1,m + 1):
    s_l.append(s[-i])
s_r = list(reversed(s))
s_f_r = list(reversed(s_f))
s_l_r = list(reversed(s_l))
if s_r == s:
    if s_f_r == s_f and s_l_r == s_l:
        print("Yes")
    else:
        print("No")
else:
    print("No")


