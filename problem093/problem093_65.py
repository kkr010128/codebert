import sys
import resource
sys.setrecursionlimit(10000)
n,k=map(int,input().rstrip().split())
p=list(map(int,input().rstrip().split()))
c=list(map(int,input().rstrip().split()))
def find(start,now,up,max,sum,count,flag):
    if start==now:
        flag+=1
    if start==now and flag==2:
        return [max,sum,count]
    elif count==up:
        return [max,sum,count]
    else:
        count+=1
        sum+=c[p[now-1]-1]
        if max<sum:
            max=sum
        return find(start,p[now-1],up,max,sum,count,flag)
kara=[-10000000000]
for i in range(1,n+1):
    m=find(i,i,n,c[p[i-1]-1],0,0,0)
    if m[2]>=k:
        m=find(i,i,k,c[p[i-1]-1],0,0,0)
        if m[0]>kara[0]:
            kara[0]=m[0]
        result=kara[0]
    elif m[1]<=0:
        if m[0]>kara[0]:
            kara[0]=m[0]
        result=kara[0]
    else:
        w=k%m[2]
        if w==0:
            w=m[2]
        spe=find(i,i,w,c[p[i-1]-1],0,0,0)[0]
        if m[1]+spe>m[0] and m[1]*(k-w)//m[2]+spe>kara[0]:
            kara[0]=m[1]*(k-w)//m[2]+spe
        elif m[1]+spe<=m[0] and m[1]*((k-w)//m[2]-1)+m[0]>kara[0]:
            kara[0]=m[1]*((k-w)//m[2]-1)+m[0]
        result=kara[0]
print(result)