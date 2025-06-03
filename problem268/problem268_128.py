mod = 1000000007

N = int(input())
A = list(map(int, input().split()))

C = [0,0,0]
ans = 1
i = 0
while i < N:
  a = A[i]
  cnt = sum([1 if C[j] == a else 0 for j in range(3)])
  ans = (ans*cnt)%mod
  if C[0] == a:
    C[0] += 1
  elif C[1] == a:
    C[1] += 1
  else:
    C[2] += 1
  i += 1
print(ans)