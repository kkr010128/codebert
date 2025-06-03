#ITP1_6_C
A=[[[0 for k in range(10)]for j in range(3)]for i in range(4)]
format(A)
n=int(input())
for m in range(n):
  b,f,r,v=map(int,input().split())
  S=A[b-1][f-1][r-1]+v
  A[b-1][f-1][r-1]=S
for i in range(4):
  for j in range(3):
    for k in range(10):
      print ("",A[i][j][k],end='')
    print("")
  if i<3:
    print("####################")
  


