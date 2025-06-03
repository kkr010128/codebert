# N=int(input())
A,B=[int(x) for x in input().rstrip().split()]

if A<=B*2:
  print(0)
else:
  print(A-B*2)