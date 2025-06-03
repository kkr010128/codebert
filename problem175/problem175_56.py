n=int(input())
s=list(input())

r=[]
g=[]
b=[]
for i in range(n):
    if s[i]=='R':
        r.append(i)
    elif s[i]=='G':
        g.append(i)
    else:
        b.append(i)

import bisect
def binary_search(a, x):
    # 数列aのなかにxと等しいものがあるか返す
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False

ans=0
for i in range(len(r)):
    for j in range(len(g)):
        p=0
        if r[i]<g[j]:
            if binary_search(b,g[j]-r[i]+g[j]):
                p+=1
            if binary_search(b,r[i]+(g[j]-r[i])/2):
                p+=1
            if binary_search(b,r[i]-(g[j]-r[i])):
                p+=1
        else:
            if binary_search(b,r[i]-g[j]+r[i]):
                p+=1
            if binary_search(b,g[j]+(r[i]-g[j])/2):
                p+=1
            if binary_search(b,g[j]-(r[i]-g[j])):
                p+=1
        ans+=len(b)-p

print(ans)




