from math import gcd
n=int(input())
a=list(map(int,input().split()))
g=gcd(a[0],a[1])
for i in range(n-2):
    g=gcd(g,a[i+2])
if a==[1]*n:
    print("pairwise coprime")
    exit()
if g!=1:
    print("not coprime")
    exit()
temp=[i for i in range(10**6+5)]
p=2
while p*p<=10**6+5:
    if temp[p]==p:
        for q in range(2*p,10**6+5,p):
            if temp[q]==q:
                temp[q]=p
    p+=1
ans=[0]*(10**6+10)
for j in a:
    count=set()
    while j>1:
        count.add(temp[j])
        j//=temp[j]
    for k in count:
        ans[k]+=1
if max(ans)!=1:
    print("setwise coprime")
else:
    print("pairwise coprime")
