a = int(input())
s = 0
b = 1
while 15*b <= a:
  s += 8*b
  b += 1
while 5*b <= a:
  s -= 7*b
  b += 1
while 3*b <= a:
  s -= 2*b
  b += 1
while b <= a:
  s += b
  b += 1
print(s)