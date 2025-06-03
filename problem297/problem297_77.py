N = int(input())

if N == 1:
  print(1)
elif N%2 == 0:
  print(0.5)
else:
  print((N+1)/2/N)