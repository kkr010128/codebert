import sys
def input():
    return sys.stdin.readline()[:-1]
N,D,A=map(int,input().split())
s=[tuple(map(int, input().split())) for i in range(N)]
s.sort()
d=2*D+1
t=0
p=0
l=[0]*N
a=0
for n,i in enumerate(s):
    while 1:
        if t<N and s[t][0]<i[0]+d:
            t+=1
        else:
            break
    h=i[1]-p*A
    if h>0:
        k=-(-h//A)
        a+=k
        p+=k
        l[t-1]+=k
    p-=l[n]
print(a)