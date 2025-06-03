ln=10**6+10
sieve=[i for i in range(ln)]
p=2
while p**2<=ln:
  if sieve[p]==p:
    for q in range(p*2,ln,p):
      if sieve[q]==q:
        sieve[q]=p
  p+=1
import collections
def primef(n):
  prime_count=collections.Counter()    
  while n>1:
    prime_count[sieve[n]]+=1
    n//=sieve[n]   
  return prime_count
n=int(input())
ans=0
for i in range(1,n):
  t=1
  for j in primef(i).values():
    t=t*(j+1)
  ans+=t
print(ans)