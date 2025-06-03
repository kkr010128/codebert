from collections import Counter
n,p = map(int,input().split())
s = input()
n = len(s)
mod = [0] * (n+1)
ten = [0] * n

a = 1
for i in range(n):
    ten[i] = a
    a = a * 10 % p

ans = 0
if p != 2 and p != 5:
    rui = 0
    for i in range(n):
        rui = (int(s[n-1-i]) * ten[i] + rui) % p
        mod[n-1-i] = rui

    b = Counter(mod)
    c = list(b.values())
    c.sort(reverse = True)

    for i in c:
        if i > 1:
            ans += i * (i-1) // 2
        else:
            break
            
elif p == 2:
    for i in range(n):
        if int(s[i]) % 2 == 0:
            ans += i+1
else:
    for i in range(n):
        if int(s[i]) % 5 == 0:
            ans += i+1

print(ans)