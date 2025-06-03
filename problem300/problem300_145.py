def gcd(a,b):
  while b:a,b=b,a%b
  return a
def divisor(n):
  ass=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      ass.append(i)
      if i!=n//i:ass.append(n//i)
  return ass
def is_prime(n):
  if n==1:return True;return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:return False
  return True
ans=0
a,b=map(int,input().split())
for i in divisor(gcd(a,b)):
  if is_prime(i):ans+=1
print(ans)