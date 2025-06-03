N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7
color = [0]*3
ans = 1
for i in range(N):
  if A[i] not in color:
    ans = 0
    break
  ind = color.index(A[i])
  ans *= len([c for c in color if c == A[i]])
  ans %= mod
  color[ind] += 1

#ans = rec(color,0)
print(ans)