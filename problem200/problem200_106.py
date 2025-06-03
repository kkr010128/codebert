A, B, M = map(int, input().split())

price_A = list(map(int, input().split()))
price_B = list(map(int, input().split()))

ans = min(price_A)+min(price_B)

for m in range(M):
  x, y, c = map(int, input().split())
  p1 = price_A[x-1] + price_B[y-1] - c
  if p1 <= ans: ans=p1

print(ans)