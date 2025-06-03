from math import sqrt
N=int(input())

for i in range(int(sqrt(N)),0,-1):
  j = N/i
  if j == int(j):
    print(int(i+j-2))
    break