x='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from collections import Counter
c=Counter([])
for i in range(len(x)):
    c[x[i]]=i
n=int(input())
s=input()
ans=''
for i in range(len(s)):
    m=c[s[i]]
    ans+=x[(m+n)%26]
print (ans)