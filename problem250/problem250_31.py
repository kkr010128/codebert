isprime = [True] * 100201

def seive(n): 
  isprime[0] = isprime[1] = False
  p = 2
  while (p*p <= n):
    if isprime[p]:
      for i in range(p*p, n+1, p):
        isprime[i] = False   
    p += 1
      
  prime = [j for j in range(n) if isprime[j]]
  return prime

		
def program():
  x = int(input())
  N = 100200
  prime = seive(N) 
    
  for i in range(len(prime)):
    if prime[i] >= x:
      return prime[i]
      break
		
print(program())
