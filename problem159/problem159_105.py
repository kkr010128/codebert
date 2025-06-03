X = int(input())
A = 100
for i in range(10**5):
  A = A*101//100
  if X <= A:
    break
print(i+1)