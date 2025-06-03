N = int(input())
A = [int(i) for i in input().split()]

temp = 0
for i in A:
  temp ^= i
  
for i in A:
  print(temp ^ i)