def is_prime(n): 
  i = 2
  while i * i <=n:
    if n % i == 0:
      return False
    i += 1
  return True

n = int(input())
data = []
[data.append(int(input())) for i in range(n)]

check = [is_prime(d) for d in data]
print(sum(check))