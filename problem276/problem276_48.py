N = int(input())
A = list(map(int,input().split()))
SUM = sum(A)
half = SUM//2
acc = 0;dif = SUM
for i in range(N):
  acc += A[i]
  dif = min(dif,abs(SUM-2*acc))

print(dif)
