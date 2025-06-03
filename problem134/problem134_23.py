n = int(input())
A = [int(i) for i in input().split()]
product = 1
A.sort()

for i in range(n):
  product *= A[i]
  if(product > 10**18):
    print("-1")
    break

if(product <= 10**18):
  print(product)