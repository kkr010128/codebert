import math
          
def koch(n, h, i, j, k):
 if n == 0:
  return
           
 sx = (h*2+j)/3
 sy = (i*2+k)/3
 tx = (h+j*2)/3
 ty = (i+k*2)/3
 ux = (tx-sx)*math.cos(math.pi/3) - (ty-sy)*math.sin(math.pi/3) + sx
 uy = (tx-sx)*math.sin(math.pi/3) + (ty-sy)*math.cos(math.pi/3) + sy
          
 koch(n-1, h, i, sx, sy)
 print sx, sy
 koch(n-1, sx, sy, ux, uy)
 print ux, uy
 koch(n-1, ux, uy, tx, ty)
 print tx, ty
 koch(n-1, tx, ty, j, k)
   
n = input()
          
px = float(0)
py = float(0)
qx = float(100)
qy = float(0)
          
print px, py
koch(n, px, py, qx, qy)
print qx, qy