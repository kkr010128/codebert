n,p = tuple(int(x) for x in input().split())
s = [int(s) for s in input()][::-1]
modlist = [0]*p
modlist[0] = 1
if p!= 2 and p != 5:
    mod = 0
    pwrmod = 1
    for i in s:
        mod = (mod + pwrmod * i) % p
        pwrmod = (pwrmod * 10) % p
        modlist[mod] += 1
    ans = 0
    for i in modlist:
        ans += (i * (i-1)) // 2

    print(ans)
else:
    ans = 0
    for i in range(n):
        if s[i] % p == 0:
            ans += n-i
    print(ans)
