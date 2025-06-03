#!/usr/bin/env python3
n,p = map(int,input().split())
s=input()
ans = 0
l = [0 for i in range(p)]
l[0] = 1
z = 0
ten = 1
tmp = 0
if p == 2 or p == 5:
    if p == 2:
        for i in range(n):
            if int(s[i])%2 == 0:
                ans+=i+1
    if p == 5:
        for i in range(n):
            if int(s[i])%5 == 0:
                ans+= i+1
    
else:
    for i in s[::-1]:
        i = int(i)
        tmp=(tmp+i*ten)%p
        ten = (ten*10)%p
        l[tmp]+=1
for i in l:
    ans+= i*(i-1)//2
print(ans)

