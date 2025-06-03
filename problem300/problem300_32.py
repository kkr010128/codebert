from fractions import gcd

A,B = map(int,input().split())
C = gcd(A,B)
nse = set()

for i in range(1,int(C**0.5+1)):
  if C%i == 0:
    nse.add(i)
    nse.add(C//i)
    
nli = list(nse)
nli.sort()
size = len(nli)

for i in range(1,size):
  n = nli[i]
  for j in range(i+1,size):
    if nli[j]%n == 0 :
      nse.add(nli[j])
      nse.remove(nli[j])

print(len(nse))