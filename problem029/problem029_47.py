x1,y1,x2,y2=map(float, input().split())

if x1<x2:
    x1,x2=x2,x1
if y1<y2:
    y1,y2=y2,y1

n=((x1-x2)**2+(y1-y2)**2)**(1/2)
print(n)
