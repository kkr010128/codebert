N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
AX = [A[i][0] for i in range(N)]
BX = [A[i][1] for i in range(N)]
AX.sort()
BX.sort()
if N % 2 == 1:
  L = AX[(N-1)//2]
  R = BX[(N-1)//2]
  print(R-L+1)
else:
  L = AX[N//2-1] + AX[N//2]
  R = BX[N//2-1] + BX[N//2]
  print(R-L+1)
