import math
def dist(a,b,n):
    s=0
    m=0
    for i in range(len(a)):
        d=math.fabs(b[i]-a[i])
        m=max(m,d)
        s+=d**n
    return (s**(1/n),m)

n=int(input())
a=list(map(float,input().split()))
b=list(map(float,input().split()))
print('%.6f'%(dist(a,b,1)[0]))
print('%.6f'%(dist(a,b,2)[0]))
print('%.6f'%(dist(a,b,3)[0]))
print('%.6f'%(dist(a,b,1)[1]))