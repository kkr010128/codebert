N = int(input())
A = list(map(int, input().split()))

ans = float('inf')
sum_A = sum(A)
hoge = 0


for i in range(N-1):
  hoge = hoge + A[i]
  ans = min(ans,abs(sum_A - (hoge*2)))

print(ans)
