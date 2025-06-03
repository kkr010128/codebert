a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
tmp = 0

if c < b:
  tmp = b
  b = c 
  c = tmp

if b < a:
  tmp = a
  a = b
  b = tmp

if c < b:
  tmp = b
  b = c
  c = tmp

print (str(a) + " " + str(b) + " " + str(c))

