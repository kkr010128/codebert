N = int(input())
A = []

for n in range(1,10):
  for m in range(1,10):
    A.append(n*m)

if N in A:
  print("Yes")
else:
  print("No")