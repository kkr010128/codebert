import math
n = int(input())
 
def koch(n, p1_x, p2_x, p1_y, p2_y):
  if n == 0:
    return
 
  s_x = (2*p1_x + p2_x) / 3
  s_y = (2*p1_y + p2_y) / 3
  t_x = (p1_x + 2*p2_x) / 3
  t_y = (p1_y + 2*p2_y) / 3
 
  u_x = (t_x - s_x)/2 - (t_y - s_y) * math.sqrt(3)/2 + s_x
  u_y = (t_x - s_x) * math.sqrt(3)/2 + (t_y - s_y)/2 + s_y
 
  koch(n-1, p1_x, s_x, p1_y, s_y)
  print (s_x, s_y)
  koch(n-1, s_x, u_x, s_y, u_y)
  print (u_x, u_y)
  koch(n-1, u_x, t_x, u_y, t_y)
  print (t_x, t_y)
  koch(n-1, t_x, p2_x, t_y, p2_y)
 
p1_x = 0.0
p1_y = 0.0
p2_x = 100.0
p2_y = 0.0
 
print (p1_x, p1_y)
koch(n, 0, 100, 0, 0)
print (p2_x, p2_y)