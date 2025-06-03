import math
#import matplotlib.pyplot as plt

def kock(n,p1,p2):
    #global x
    #global y
    if n==0:
        return
    s=[0,0]
    t=[0,0]
    u=[0,0]
    
    s[0]=(float((2*p1[0]+p2[0])/3))
    s[1]=(float((2*p1[1]+p2[1])/3))
    t[0]=(float((p1[0]+2*p2[0])/3))
    t[1]=(float((p1[1]+2*p2[1])/3))

    u[0]=((t[0]-s[0])*math.cos(math.radians(60))-(t[1]-s[1])*math.sin(math.radians(60))+s[0])
    u[1]=((t[0]-s[0])*math.sin(math.radians(60))+(t[1]-s[1])*math.cos(math.radians(60))+s[1])
    


    kock(n-1,p1,s)
    print(*s)
   # x.append(s[0])
    #y.append(s[1])
    kock(n-1,s,u)
    print(*u)
    #x.append(u[0])
    #y.append(u[1])
    kock(n-1,u,t)
    print(*t)
    #x.append(t[0])
    #y.append(t[1])
    kock(n-1,t,p2)



n=int(input())
p1=[0.0,0.0]
p2=[100.0,0.0]
#x=[]
#y=[]
print(*p1)
#x.append(p1[0])
#y.append(p1[1])
kock(n,p1,p2)
print(*p2)

