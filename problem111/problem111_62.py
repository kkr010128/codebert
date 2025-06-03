N = int(input())
A = list(map(int,input().split()))

A = sorted(A,reverse=True)

if N <= 3:
  ans = sum(A[:-1])
elif N % 2 == 0:
  ans = A[0] + sum(A[1:(N-2)//2+1])*2
elif N % 2 == 1:
  ans = A[0] + sum(A[1:(N-2)//2+1])*2 + A[1+(N-2)//2]
  
print(ans)
