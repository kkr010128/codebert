N = int(input())
A = list(map(int,input().split()))
A = sorted(A,reverse=True)

ans = A[0]

for i in range(1,(N-2)//2+1):
  ans += A[i]*2
  
if N % 2 == 1:
  ans += A[(N-2)//2 + 1]

print(ans)