N = int(input())
A = list(map(int,input().split()))
Ans = 1

if 0 in A:
  Ans = 0

else:
  for i in range(0,N):
    Ans *= A[i]
    if Ans > 1000000000000000000:
      Ans = -1
      break
    
print(Ans)
