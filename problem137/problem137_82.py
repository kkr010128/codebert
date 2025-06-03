N = int(input())
As = []
Bs = []
for i in range(N):
  A, B = map(int, input().split())
  As.append(A)
  Bs.append(B)
As.sort()
Bs.sort()
if N%2 == 1:
  A = As[N//2]
  B = Bs[N//2]
  r = B-A+1
else:
  A = As[(N-1)//2]+As[N//2]
  B = Bs[(N-1)//2]+Bs[N//2]
  r = B-A+1
print(r)
