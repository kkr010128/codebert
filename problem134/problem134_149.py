n=int(input())
A=list(map(int,input().split()))
x=1
A.sort()
if 0 in A:
  print(0)
  exit()

for i in range(n):
  x*=A[n-i-1]
  if x>10**18:
    print(-1)
    exit()
  else:
    continue

print(x)