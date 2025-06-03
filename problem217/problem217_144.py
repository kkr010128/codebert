N = int(input())
A = list(map(int,input().split()))
x = True

for i in range(N):
  if A[i] % 2 != 0:
    continue
  if not (A[i]%3==0 or A[i]%5==0):
    x = False
if x:
  print("APPROVED")
else:
  print("DENIED")