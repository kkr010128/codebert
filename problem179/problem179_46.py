n, m = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)

ans = 0
for a in A:
  if 4 * a * m >= sumA:
    ans += 1
    
if ans >= m:
  print("Yes")
else:
  print("No")
