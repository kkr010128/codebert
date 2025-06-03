import math

n=int(input())

#def koch(p1,p2,n):
def koch(d,p1,p2):
  if d==0:
    return
  #3等分する
  s=[(2*p1[0]+1*p2[0])/3,(2*p1[1]+1*p2[1])/3]
  t=[(1*p1[0]+2*p2[0])/3,(1*p1[1]+2*p2[1])/3]
  #正三角形の頂点のひとつである座標を求める
  u=[
    (t[0]-s[0])*math.cos(math.radians(60))-(t[1]-s[1])*math.sin(math.radians(60))+s[0],
    (t[0]-s[0])*math.sin(math.radians(60))+(t[1]-s[1])*math.cos(math.radians(60))+s[1]
    ]
  koch(d-1,p1,s)
  print(*s)
  koch(d-1,s,u)
  print(*u)
  koch(d-1,u,t)
  print(*t)
  koch(d-1,t,p2)

print('0 0')
koch(n,[0,0],[100,0])
print('100 0')
