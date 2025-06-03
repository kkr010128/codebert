def gcd (a,b):
  if a%b==0:
    return b
  if b%a==0:
    return a
  if a>b:
    return gcd(b,a%b)
  return gcd(a,b%a)
def lcm (a,b):
  return ((a*b)//gcd(a,b))
inp=list(map(int,input().split()))
a=inp[0]
b=inp[1]
print (lcm(a,b))