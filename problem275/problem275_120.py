x,y=map(int,input().split())
c=0
d=0
if x==1:
    c=300000
elif x==2:
    c=200000
elif x==3:
    c=100000
if y==1:
    d=300000
elif y==2:
    d=200000
elif y==3:
    d=100000
print(c+d if c+d!=600000 else 1000000)