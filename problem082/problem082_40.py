s = input()
t = input()
s_l = len(s)
t_l = len(t)
s_l -= (t_l-1)
if(t in s):
    print(0)
    exit()

ma = 0
for si in range(s_l):
    cnt = 0
    for ti in range(t_l):
        if(s[si+ti]==t[ti]):
            cnt += 1
    ma = max(ma,cnt)

print(t_l - ma)
