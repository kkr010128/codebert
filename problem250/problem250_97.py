X = int(input())
MAX = 10**5+3
num = 2
primes = [0 for _ in range(MAX+1)]


for num in range(2, int(MAX**0.5)):
  if primes[num] == 1:
    continue
  for i in range(num*2, MAX+1, num):
    primes[i] = 1
for num in range(X, MAX+1):
  if primes[num] == 0:
    print(num)
    exit()



  
  
