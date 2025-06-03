import math
class Point(object):
     def __init__(self, x,y):
          self.x = x*1.0
          self.y = y*1.0
def Koch(n,p1,p2):
    s=Point((2*p1.x+p2.x)/3,(2*p1.y+p2.y)/3)
    t=Point((p1.x+2*p2.x)/3,(p1.y+2*p2.y)/3)
    u=Point((t.x-s.x)*math.cos(math.radians(60))-(t.y-s.y)*math.sin(math.radians(60))+s.x,(t.x-s.x)*math.sin(math.radians(60))+(t.y-s.y)*math.cos(math.radians(60))+s.y)
    if n==0:
        return
    Koch(n-1,p1,s)
    print s.x,s.y
    Koch(n-1,s,u)
    print u.x,u.y 
    Koch(n-1,u,t)
    print t.x,t.y
    Koch(n-1,t,p2)
n=input()
p1=Point(0,0)
p2=Point(100,0)
print p1.x,p1.y
Koch(n,p1,p2)
print p2.x,p2.y
