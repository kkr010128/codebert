N = int(input())
A, B = [], []
for i in range(N):
  a, b = map(int, input().split())
  A += [a]
  B += [b]

A.sort()
B.sort()
if N%2 == 1:
  med_minimum = A[(N-1)//2]
  med_maximum = B[(N-1)//2]
else:
  med_minimum = (A[(N-2)//2] + A[(N-2)//2+1])
  med_maximum = (B[(N-2)//2] + B[(N-2)//2+1])
print(med_maximum - med_minimum + 1)
