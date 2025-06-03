import math
def kock(n,p1,p2):
    if n==0:
        return
    s=[(2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3]
    t=[(p1[0]+2*p2[0])/3,(p1[1]+2*p2[1])/3]
    kock(n-1,p1,s)
    print(*s)
    u=[(t[0]-s[0])*math.cos(math.radians(60))-(t[1]-s[1])*math.sin(math.radians(60))+s[0],(t[0]-s[0])*math.sin(math.radians(60))+(t[1]-s[1])*math.cos(math.radians(60))+s[1]]
    kock(n-1,s,u)
    print(*u)
    kock(n-1,u,t)
    print(*t)
    kock(n-1,t,p2)

n=int(input())
p1=[0,0]
p2=[100,0]
print(*p1)
kock(n,p1,p2)
print(*p2)
