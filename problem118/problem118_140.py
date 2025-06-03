N = int(input())

A = [1] * (N+1)
for i in range(2,N+1):
  a = i
  while a < N+1:
    A[a] += 1
    a += i

#print(A)
ans = 0
for i in range(N+1):
  ans += i * A[i]
  
print(ans)