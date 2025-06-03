n=int(input())
p=[[0,0]]
r3=1.7320508
def unit_koch(p1,p2,d):
  if d>=n:
    return
  s=[(p1[0]*2+p2[0])/3,(p1[1]*2+p2[1])/3]
  t=[(p1[0]+p2[0]*2)/3,(p1[1]+p2[1]*2)/3]
  v_s_t=[t[0]-s[0],t[1]-s[1]]
  v_s_u=[v_s_t[0]/2-v_s_t[1]*r3/2,v_s_t[1]/2+v_s_t[0]*r3/2]
  u=[s[0]+v_s_u[0],s[1]+v_s_u[1]]
  unit_koch(p1,s,d+1)
  p.append(s)
  unit_koch(s,u,d+1)
  p.append(u)
  unit_koch(u,t,d+1)
  p.append(t)
  unit_koch(t,p2,d+1)
unit_koch([0,0],[100,0],0)
p.append([100,0])
for i in p:
  print(str(i[0])+' '+str(i[1]))
