a,b=map(int,input().split())

def gcd(a,b):
  if a<b:
    a,b=b,a
  while a%b:
    a,b=b,a%b
  return b

g=gcd(a,b)

f=set()
for i in range(1,int(g**0.5)+1):
  if g%i==0:
    for j in range(2,int(i**0.5)+1):
      if i%j==0:
        break
    else:
      f.add(i)
    p=g//i
    for j in range(2,int(p**0.5)+1):
      if p%j==0:
        break
    else:
      f.add(p)

print(len(f))