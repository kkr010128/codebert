N = int(input())
m = 1000
k = 0
A = list(map(int,input().split()))
M = A[0]
for a in A:
  if M > a:
    if k > 0:
      m += k * M
      k = 0
  elif M < a:
    if k == 0:
      k,m = divmod(m,M)
  M = a
m += k * M
print(m)