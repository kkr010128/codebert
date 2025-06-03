from functools import reduce
n=int(input())
A=list(map(int, input().split()))
sumxor=reduce(lambda x,y:x^y,A)
for AA in A:
  print(sumxor ^ AA)