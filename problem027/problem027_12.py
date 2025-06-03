import math

def curve(inp):
    ret = []
    n = len(inp)
    cos60 = math.cos(math.radians(60))
    sin60 = math.sin(math.radians(60))
    for i in range(n - 1):
        p1x, p1y = inp[i]
        p2x, p2y = inp[i+1]
        
        diffx = (p2x - p1x) / 3
        diffy = (p2y - p1y) / 3
        sx, sy = p1x + diffx, p1y + diffy
        ux = sx + diffx * cos60 - diffy * sin60
        uy = sy + diffx * sin60 + diffy * cos60
        tx, ty = p2x - diffx, p2y - diffy
        
        ret.extend([(p1x, p1y), (sx, sy), (ux, uy), (tx, ty)])
    ret.append(inp[-1])
        
    return ret
      
      
if __name__=="__main__":
    inp = [(0.0, 0.0), (100.0, 0.0)]
    N = int(input())
    for i in range(N):
        inp = curve(inp)
    for i in inp:
      print(*i)
