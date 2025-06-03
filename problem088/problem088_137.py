N = int(input())
A = list(map(int, input().split()))
ans = 0
h = A[0]
for a in A:
  if h > a:
    ans += h - a
  else:
    h = a
print(ans)