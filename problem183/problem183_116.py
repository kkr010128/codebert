def divisor(n):
  ret=[]
  for i in range(1,int(n**0.5)+1):
    if n%i==0:
      a,b=i,n//i
      if a!=b:
        ret+=a,
        ret+=b,
      else:
        ret+=a,
  return sorted(ret)

def f(n):
  return divisor(n)[1:]

def solve(n):
  ans=f(n-1)
  for k in f(n):
    N=n
    while N>=k:
      if N%k==0:N=N//k
      else:N=N%k
    if N==1:ans+=k,
  print(len(ans))
  return 0

solve(int(input()))