L,R,d=(int(x) for x in input().split())
a=R//d
b=L//d
c=a-b
if L % d == 0:
  c=c+1
print(c)