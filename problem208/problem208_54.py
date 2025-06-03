A=list()
B=list()
n,m=map(int,input().split())
if m==0:
  print([0, 10, 100][n - 1])
  exit()
for i in range(m):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
  if a==1 and b==0 and n!=1:
    print(-1)
    exit()
for i in range(1000):
  c=str(i)
  if len(c)==n:
    for j in range(m):
      if c[A[j]-1]!=str(B[j]):
        break
      if j==m-1:
        print(i)
        exit()
print(-1)