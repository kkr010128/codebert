import math

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

def koch(n, p1, p2):
    if n == 0:
        return str(p2.x) + " " + str(p2.y)
    
    else:
        s = coordinate((2*p1.x + p2.x)/3, (2*p1.y + p2.y)/3)
        t = coordinate((p1.x + 2*p2.x)/3, (p1.y + 2*p2.y)/3)
        u = coordinate((t.x-s.x)/2-(t.y-s.y)/2*math.sqrt(3)+s.x, (t.x-s.x)/2*math.sqrt(3)+(t.y-s.y)/2+s.y)
        print(koch(n-1, p1, s))
        print(koch(n-1, s, u))
        print(koch(n-1, u, t))
        return(koch(n-1, t, p2))


q1 = coordinate(0.00000000, 0.00000000)
q2 = coordinate(100.00000000, 0.00000000)

print(str(q1.x) + " " + str(q1.y))
print(koch(int(input()), q1, q2))

