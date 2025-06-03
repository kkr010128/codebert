import math
def kock(n, p1, p2):
 if n == 0:
  return

 #p1.p2??????s,t,u????¨????
 sx = (2 * p1[0] + 1 * p2[0]) / 3
 sy = (2 * p1[1] + 1 * p2[1]) / 3
 s = [sx, sy]
 tx = (1 * p1[0] + 2 * p2[0]) / 3
 ty = (1 * p1[1] + 2 * p2[1]) / 3
 t = [tx, ty]
 ux = (tx-sx) * math.cos(math.radians(60)) - (ty-sy) * math.sin(math.radians(60)) + sx
 uy = (tx-sx) * math.sin(math.radians(60)) + (ty-sy) * math.cos(math.radians(60)) + sy
 u = [ux, uy]

 kock(n-1,p1,s)
 print(" ".join(['{:.5f}'.format(i) for i in s]))
 kock(n-1,s,u)
 print(" ".join(['{:.5f}'.format(i) for i in u]))
 kock(n-1,u,t)
 print(" ".join(['{:.5f}'.format(i) for i in t]))
 kock(n-1,t,p2)

n = float(input())
print("0.00000 0.00000")
kock(n, [0,0], [100,0])
print("100.00000 0.00000")