N = int(input())
A = [int(a) for a in input().split()]

if A.count(0):
  print(0)
  exit(0)

ans=1
for a in A:
  ans *= a
  if ans > 10**18:
    print(-1)
    break
else:
  print(ans)
