a,b,c = map(int, raw_input().split())

if a > b:
  temp = a
  a = b
  b = temp
if b > c:
  temp = b
  b = c
  c = temp
if a > b:
  temp = a
  a = b
  b = temp

print a,b,c