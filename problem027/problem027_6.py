n = int(input())

def three_points(p1,p2):
    q1 = ((2*p1[0]+p2[0])/3, (2*p1[1]+p2[1])/3)
    q2 = ((p1[0]+2*p2[0])/3, (p1[1]+2*p2[1])/3)
    dx,dy = p2[0]-p1[0], p2[1]-p1[1]
    q3 = (p1[0]+dx/2-3**0.5/6*dy, p1[1]+dy/2+3**0.5/6*dx)
    return [q1,q3,q2]

m = [(0,0),(100,0)]
for i in range(n):
    tmpm = []
    for j in range(len(m)-1):
        tmpm += [m[j]] + three_points(m[j],m[j+1])
    tmpm += [m[-1]]
    m = tmpm

for x in m:
    print(x[0], x[1])
