a=1
b=1
c=[]
n=int(input())
c.append(a)
c.append(b)
for i in range(n):
  c.append(a+b)
  d=b
  b+=a
  a=d
print(c[n])
