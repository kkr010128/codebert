from functools import reduce
def nCr(n,r,DIV):
  if r<n-r:
    r=n-r
  if r==0:
    return 1
  f=lambda x,y:x*y%DIV
  X=reduce(f,range(n-r+1,n+1))
  Y=reduce(f,range(1,r+1))
  return X*pow(Y,DIV-2,DIV)%DIV

mod = pow(10, 9) + 7
x, y = map(int, input().split())
left, right = 0, 0
a, b = max(x, y), min(x, y)

if (2*b - a) % 3 == 0:
    d, s = a - b, (2*b - a)//3
    p, q = d + s, s
    print(nCr(p+q, p, mod))
else:
    print(0)