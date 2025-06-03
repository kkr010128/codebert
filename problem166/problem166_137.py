from collections import Counter

n = list(input())
n.reverse()
x = [0]*(len(n))
a=0
ex=1
for i in range(len(n)):
    a+=int(n[i])*ex
    x[i]=a%2019
    ex=ex*10%2019
c=Counter(x)
ans = c[0]
for i in c.keys():
    b=c[i]
    ans += b*(b-1)//2

print(ans)
