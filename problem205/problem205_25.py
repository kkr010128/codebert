n,p = map(int,input().split())
s = input()
l = [0 for i in range(p)]
l[0] = 1
ten = 1
cnt = 0

ans = 0
if p == 2 or p == 5:
    for i in range(n):
        if int(s[i]) % p == 0:
            ans += i+1
else:
    for i in range(n):
        cnt = (cnt + int(s[-i-1]) * ten) % p
        l[cnt] += 1
        ten = (ten * 10) % p
    for i in l:
        if i > 1:
            ans += i * (i - 1) // 2

print(ans)