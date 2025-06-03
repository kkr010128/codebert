N = int(input())
A = [[0]*10 for _ in range(10)]
for i in range(1,N+1):
  a = i%10 #1の位
  b = i // (10**(len(str(i))-1))
  if a!= 0:
    A[a][b] += 1
t = 0
for i in range(1,10):
  s = A[i][i]
  if s != 0:
    t += int(s + (s*(s-1)))
for i in range(1,9):
  for j in range(i+1,10):
    t += A[i][j] * A[j][i]*2
print(t)