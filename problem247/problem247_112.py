n,m=map(int,input().split())
l=list(map(int,input().split()))
l=list(set(l))
n=len(l)
ll=[]
for i in l:
    ll.append(int(i/2))

newl=[]
for i in ll:
    j=i
    count=0
    while j%2==0:
        j//=2
        count+=1
    newl.append(count)
import collections
newl=collections.Counter(newl)
if len(newl)!=1:
    print(0)
     
else:
    from fractions import gcd
    num=ll[0]
    flag=True
    for i in ll:
        if num<=m:
            num=int(i*num/gcd(i,num))
        else:
            flag=False
            break
    if flag==False:
        print(0)
    else:
        k=m%(num*2)
        if k>=num:
            print(int(m//(num*2)+1))
        else:
            print(int(m//(num*2)))