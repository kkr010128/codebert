import math

def CalcCoordinate(xa, ya, xb, yb):
    arg = math.atan2(yb-ya, xb-xa) #角度
    d = math.sqrt((xb-xa)*(xb-xa) + (yb-ya)*(yb-ya)) #AとBの距離
    xc = d/2 #ピタゴラスの定理より
    #S = math.sqrt(3)*d*d/2
    #正三角形にヘロンの公式を適用(3辺の長さが同じなので3*d)
    yc = math.sqrt(3)*d/2

    #if(yb <= ya):
    ux = xc*math.cos(arg) - yc*math.sin(arg) + xa
    uy = xc*math.sin(arg) + yc*math.cos(arg) + ya
    return ux, uy
    """
    else:
        ux = xc*math.cos(arg) + yc*math.sin(arg) + xa
        uy = xc*math.sin(arg) - yc*math.cos(arg) + ya
        return ux, uy
"""

def MakeTriangle(x1, y1, x2, y2, n):
    if(n != 0):
        sx = (2*x1 + x2) / 3
        sy = (2*y1 + y2) / 3
        tx = (x1 + 2*x2) / 3
        ty = (y1 + 2*y2) / 3
        ux, uy = CalcCoordinate(sx, sy, tx, ty)
        MakeTriangle(x1, y1, sx, sy, n-1)
        print(sx, sy)
        MakeTriangle(sx, sy, ux, uy, n-1)
        print(ux, uy)
        MakeTriangle(ux, uy, tx, ty, n-1)
        print(tx, ty)
        MakeTriangle(tx, ty, x2, y2, n-1)
    else:
        return
        
  

x1 = 0
y1 = 0
x2 = 100
y2 = 0

n = int(input())

print(x1, y1)
MakeTriangle(x1, y1, x2, y2, n)
print(x2, y2)
