x1,y1,x2,y2=map(float,input().split())
if x1<=x2:
    x=x2-x1
else:
    x=x1-x2

if y1<=y2:
    y=y2-y1
else:
    y=y1-y2
    
t=x**2+y**2
t1=t**(1/2)
print(f'{t1:10.8f}')
