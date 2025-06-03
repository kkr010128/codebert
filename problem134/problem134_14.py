n = int(input())
A = list(map(int, input().split()))
ans = 1
A = sorted(A)
for i in range(n):
  ans *= A[i]
  if ans > 10**(18):
    print('-1')
    exit()
print(ans)