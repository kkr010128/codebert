a,b,k = map(int,input().split())

a -= k
if a <= -1:
  p = abs(a)
  a = 0
  b -= p
  if b <= -1:
    b = 0
    
print(str(a) + ' ' + str(b))