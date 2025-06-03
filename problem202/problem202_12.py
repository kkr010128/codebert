N,A,B = map(int,input().split())

if A == 0:
  print(0)
  exit(0)

first = (N // (A+B))*A
second = min(A, N % (A+B))
ans = first + second
print(ans)