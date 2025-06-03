n, d = map(int, input().split())

A = []

for i in range(n):
  A_i = list(map(int, input().split()))
  A.append(A_i)
  
ans = 0

for j in A:
  if (j[0] ** 2 + j[1] ** 2) <= d **2 :
    ans += 1

print(ans)
