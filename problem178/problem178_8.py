x,y,z=map(int,input().split())
temp=x
x=y
y=temp
temp=x
x=z
z=temp
print("{0} {1} {2}".format(x,y,z))