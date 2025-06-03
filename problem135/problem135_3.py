st = input().strip().split()
 
a = int(st[0])
b = 0
d = 0
 
for x in st[1]:
  if x == '.':
    d = 1
  else:
    b = b*10 + int(x)
    d = d*10

print(a*b//d)