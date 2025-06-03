a=int(input())
b=a//3
c=a//5
d=a//15

z=0
y=0
w=0
v=0

for x in range(a+1):
  z=z+x

for x in range(b+1):
  y=y+x*3

for x in range(c+1):
  w=w+x*5

for x in range(d+1):
  v=v+x*15

print(z-y-w+v)