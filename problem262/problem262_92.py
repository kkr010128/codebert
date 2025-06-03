N = int(input())
x = [[0] * (N-1) for _ in range(N)]
y = [[0] * (N-1) for _ in range(N)]
A = [0] * N
for i in range(N):
  A[i] = int(input())
  for j in range(A[i]):
    x[i][j], y[i][j] = list(map(int, input().split()))
n = 2 ** N
Flag = 0
ans = 0
while(n < 2 ** (N+1)):
  Flag = 0
  for i in range(N):
    if(int(bin(n)[i + 3]) == 1):
      for j in range(A[i]):
        if(y[i][j] != int(bin(n)[x[i][j] + 2])):
          Flag = 1
          break
    if(Flag == 1):
      break
  else:
    ans = max(ans, sum(list(map(int,bin(n)[3:]))))
  n += 1
print(ans)