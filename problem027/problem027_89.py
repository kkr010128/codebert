import math
INFTY=100000000

n=int(input())

def kock(p1,p2,n):
    s=[(p1[0]*2+p2[0])/3, (p1[1]*2+p2[1])/3]
    t=[(p1[0]+p2[0]*2)/3, (p1[1]+p2[1]*2)/3]
    u=[(t[0]-s[0])/2-(t[1]-s[1])/2*math.sqrt(3)+s[0], (t[0]-s[0])/2*math.sqrt(3)+(t[1]-s[1])/2+s[1]]
    if n==0:
        print("%.8f %.8f"%(p1[0],p1[1]))
    else:
        kock(p1,s,n-1)
        kock(s,u,n-1)
        kock(u,t,n-1)
        kock(t,p2,n-1)

start=[0.0,0.0]
end=[100.0, 0.0]
if n==0:
    print("%.8f %.8f"%(start[0],start[1]))
    print("%.8f %.8f"%(end[0],end[1]))
else:
    kock(start,end,n)
    print("%.8f %.8f"%(end[0],end[1]))   


