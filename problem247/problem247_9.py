def gcd_e(x, y):
  if y == 0:
    return x
  else:
    return gcd_e(y,x%y)      

def lcm(x, y):
  return (x * y) // gcd_e(x, y)

n,m=list(map(int,input().split()))
A=list(map(int,input().split()))
a,b=A[0],0

for i in range(1,n):
  b = A[i]
  a = lcm(a,b)
  
for i in set(A):
  if (a // i) % 2 == 0:
    print('0')
    exit()    
  
if a // 2 > m:
  print('0')
else:
  print((m-a//2)//a+1)