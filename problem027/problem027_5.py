import math

def KochCurve(p1,p2,n):
    if n==0:
        return
    s = [(2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3]
    t = [(p1[0]+2*p2[0])/3,(p1[1]+2*p2[1])/3]
    u = [(p1[0]+p2[0])/2+((-1)*math.sqrt(3))*(p2[1]-p1[1])/6,(p1[1]+p2[1])/2+(math.sqrt(3))*(p2[0]-p1[0])/6]
    KochCurve(p1,s,n-1)
    print(f"{'{:.9f}'.format(s[0])} {'{:.9f}'.format(s[1])}")
    KochCurve(s,u,n-1)
    print(f"{'{:.9f}'.format(u[0])} {'{:.9f}'.format(u[1])}")
    KochCurve(u,t,n-1)
    print(f"{'{:.9f}'.format(t[0])} {'{:.9f}'.format(t[1])}")
    KochCurve(t,p2,n-1)

p1 = [0,0]
p2 = [100,0]
n = int(input())
print(f"{'{:.9f}'.format(p1[0])} {'{:.9f}'.format(p1[1])}")
KochCurve(p1,p2,n)
print(f"{'{:.9f}'.format(p2[0])} {'{:.9f}'.format(p2[1])}")
