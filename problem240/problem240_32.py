n,m = map(int,input().split())
if m != 0:
    l = [list(input().split()) for i in range(m)]
    p,s = [list(i) for i in zip(*l)]
t = [0] * n
ac = 0
wa = 0
for i in range(m):
    if s[i] == 'WA' and t[int(p[i])-1] != 'AC':
        t[int(p[i])-1] += 1
    elif s[i] == 'AC' and t[int(p[i])-1] != 'AC':
        ac += 1
        wa += t[int(p[i])-1]
        t[int(p[i])-1] = 'AC'
    else:
        pass
print(ac,wa)