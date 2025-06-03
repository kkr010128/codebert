a,b = map(int, input().split())
child = a*b
if a < b:
  a,b = b,a

r = a%b
while r > 0:
  a = b
  b = r
  r = a%b

print(child//b)