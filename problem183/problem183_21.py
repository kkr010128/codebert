N=int(input())
if N==2:
  print(1)
  exit()
def make_divisors(n):
  divisors = []
  for i in range(1, int(n**0.5)+1):
    if n % i == 0:
      divisors.append(i)
      if i != n // i:
        divisors.append(n//i)

    # divisors.sort()
  return divisors
#N-1の約数(1は除く)　Nそのもの
#2
d=make_divisors(N-1)
if not 2 in d:
  d.append(2)
#print(d)
d2=make_divisors(N)
#print(len(d))
for i in d2:
  if i!=N and i!=1 and i not in d:
    now=N
    while now%i==0:
      now/=i
    if now%i==1:
      d.append(i)
print(len(d))