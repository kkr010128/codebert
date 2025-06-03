n = int(input())
L = list(map(int, input().split()))
a = L[0]
b = 0
for i in range(n-1):
  if L[i+1] < a:
    b = b + (a - L[i+1])
  else:
    a = L[i+1]
print(b)