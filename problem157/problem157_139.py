N = int(input())
A = list(map(int,input().split()))
 
ans = 0
l = [0]*N
u = [0]*N

for i in range(N):
  b = i - A[i]
  c = i + A[i]
  if 0 < b < N:
    l[b] += 1
  if 0 < c < N:
    u[c] += 1

for i in range(N):
  ans += l[i]*u[i]

print(ans)