N=int(input())
L=list(map(int,input().split()))
A=1
if 0 in L:
  print(0)
  exit()
for i in range(N):
  A=A*L[i]
  if 10**18<A:
    print(-1)
    exit()
print(A)