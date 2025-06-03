r=map(float,raw_input().split())
x=r[0]-r[2]
y=r[1]-r[3]
if x<0:
        x=x*-1
if y<0:
        y=y*-1
print (x**2+y**2)**0.5