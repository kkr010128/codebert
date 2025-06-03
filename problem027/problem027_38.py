#coding:UTF-8
import math

def KC(n,p1,p2):
    if n==0:
        return
    s=[(2*p1[0]+p2[0])/3,(2*p1[1]+p2[1])/3]
    t=[(p1[0]+2*p2[0])/3,(p1[1]+2*p2[1])/3]
    u=[(t[0]-s[0])*math.cos(math.pi/3)-(t[1]-s[1])*math.sin(math.pi/3)+s[0],(t[0]-s[0])*math.sin(math.pi/3)+(t[1]-s[1])*math.cos(math.pi/3)+s[1]]
    KC(n-1,p1,s)
    print(str(format(s[0],'.8f'))+" "+str(format(s[1],'.8f')))
    KC(n-1,s,u)
    print(str(format(u[0],'.8f'))+" "+str(format(u[1],'.8f')))
    KC(n-1,u,t)
    print(str(format(t[0],'.8f'))+" "+str(format(t[1],'.8f')))
    KC(n-1,t,p2)
    
  
if __name__=="__main__":
    n=int(input())
    p1=[0,0]
    p2=[100,0]
    print(str(format(p1[0],'.8f'))+" "+str(format(p1[1],'.8f')))
    KC(n,p1,p2)
    print(str(format(p2[0],'.8f'))+" "+str(format(p2[1],'.8f')))