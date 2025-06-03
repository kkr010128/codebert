import math
pi = math.pi

th = pi * 60.0 / 180.0
cos = math.cos(th)
sin = math.sin(th)

class Point():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
def koch(n, p1, p2):
    if n == 0:
        return None
    
    s = Point()
    t = Point()
    u = Point()
    
    s.x = (2.0 * p1.x + 1.0 * p2.x) / 3.0
    s.y = (2.0 * p1.y + 1.0 * p2.y) / 3.0
    t.x = (1.0 * p1.x + 2.0 * p2.x) / 3.0
    t.y = (1.0 * p1.y + 2.0 * p2.y) / 3.0
    u.x = (t.x - s.x) * cos - (t.y - s.y) * sin + s.x
    u.y = (t.x - s.x) * sin + (t.y - s.y) * cos + s.y
    
    koch(n-1, p1, s)
    print(s.x, s.y)
    koch(n-1, s, u)
    print(u.x, u.y)
    koch(n-1, u, t)
    print(t.x, t.y)
    koch(n-1, t, p2)
    
def main():
       
    p1 = Point()
    p2 = Point()
    
    n = int(input())
    
    p2.x = 100
    
    print(p1.x, p1.y)
    koch(n, p1, p2)
    print(p2.x, p2.y)
    
    return 0
    
if __name__ == '__main__':
    main()
