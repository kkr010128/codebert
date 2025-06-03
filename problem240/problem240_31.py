n,m = map(int,input().split())
wa = [0] * 10**6
ac = [0] * 10**6
ans = 0
for i in range(m):
    str_p,str_m = map(str,input().split())
    p = int(str_p)
    if str_m =='WA':
        if ac[p] == 0:
            wa[p] += 1
    else:
        if ac[p] == 0:
            ac[p] = 1
            ans += wa[p]
print(sum(ac),ans)