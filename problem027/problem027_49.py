import math
def kock(n,p1,p2):
    a=math.radians(60)
    if n==0:
        return 0
    s=[(2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3]
    t=[(p1[0]+2*p2[0])/3,(p1[1]+2*p2[1])/3]
    u=[((t[0]-s[0])*math.cos(a)-(t[1]-s[1])*math.sin(a))+s[0],(t[0]-s[0])*math.sin(a)+(t[1]-s[1])*math.cos(a)+s[1]]
    kock(n-1,p1,s)
    print(" ".join(map(str,s)))
    kock(n-1,s,u)
    print(" ".join(map(str,u)))
    kock(n-1,u,t)
    print(" ".join(map(str,t)))
    kock(n-1,t,p2)
n=int(input())
start=[float(0),float(0)]
end=[float(100),float(0)]
print(" ".join(map(str,start)))
kock(n,start,end)
print(" ".join(map(str,end)))
