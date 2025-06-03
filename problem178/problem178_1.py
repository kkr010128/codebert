x,y,z =map(int,input().split())
t=0
t=x;x=y;y=t;
t=x;x=z;z=t;
print(x,y,z)