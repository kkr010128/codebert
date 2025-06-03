s = input()
k = int(input())
ren = []
n = 1
p = s[0]
for i in range(1,len(s)):
    if p == s[i]:
        n += 1
    else:
        ren.append(n)
        p = s[i]
        n = 1
ren.append(n)

ans = 0
if ren[0] == len(s):
    ans = (ren[0]*k)//2
elif s[0] == s[-1]:
    ans = ren[0]//2 + ren[-1]//2 - (ren[0]+ren[-1])//2
    ren[0] += ren[-1]
    ren[-1] = 0
    for i in ren:
        ans += (i//2)*k
else:
    for i in ren:
        ans += (i//2)*k

print(ans)
