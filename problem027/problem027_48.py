import math

n = int(raw_input())

th = math.pi * 60.0 / 180.0

def split(x,y):
    s = ((2*x[0]+y[0])/3, (2*x[1]+y[1])/3)
    t = ((x[0]+2*y[0])/3, (x[1]+2*y[1])/3)
    u = ((t[0]-s[0])*math.cos(th) - (t[1]-s[1])*math.sin(th) + s[0], (t[0]-s[0])*math.sin(th) + (t[1]-s[1])*math.cos(th) + s[1])
    return (s,u,t)


s = (0.,0.)
t = (100.,0.)
points = []
points.append(s)
points.append(t)
for i in range(n):
    new_points = []
    j = 0
    while True:
        s,u,t = split(points[j],points[j+1])
        new_points.extend((points[j],s,u,t))
        j += 1
        if j+1 >= len(points): break
    new_points.append(points[j])
    points = new_points
for p in points:
    print p[0],p[1]