N = int(input())
A = list(map(int, input().split()))

ans = float('inf') 
sum_A = sum(A)
CumSum = 0


for i in range(N-1):
  CumSum = CumSum + A[i]
  ans = min(ans,(abs((sum_A - CumSum)-(CumSum))))

print(ans)
