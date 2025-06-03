import math

def Koch(Px, Py, Qx, Qy, n) :
    if n == 0 :
        return
    else :
        Ax = (2 * Px + Qx) / 3
        Ay = (2 * Py + Qy) / 3
        Bx = (Px + 2 * Qx) / 3
        By = (Py + 2 * Qy) / 3
        Cx = Ax + (Bx - Ax) * math.cos(math.pi/3) - (By - Ay) * math.sin(math.pi/3) 
        Cy = Ay + (Bx - Ax) * math.sin(math.pi/3) + (By - Ay) * math.cos(math.pi/3)
        
        Koch(Px, Py, Ax, Ay, n-1)
        print(Ax, Ay)
        Koch(Ax, Ay, Cx, Cy, n-1)
        print(Cx, Cy)
        Koch(Cx, Cy, Bx, By, n-1)
        print(Bx, By)
        Koch(Bx, By, Qx, Qy, n-1)

n = int(input())
print(0, 0.00000000)
Koch(0.00000000, 0.00000000, 100.00000000, 0.00000000, n)
print(100.00000000, 0.00000000)

