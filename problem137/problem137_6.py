N=int(input())
A=list()
B=list()
for i in range(N):
  a,b=map(int,input().split())
  A.append(a)
  B.append(b)
A.sort()
B.sort()

if N%2==1:
  print(B[int((N-1)/2+0.5)]-A[int((N-1)/2+0.5)]+1)
else:
  print((B[int(N/2+0.5)-1]+B[int(N/2+0.5)])-(A[int(N/2+0.5)-1]+A[int(N/2+0.5)])+1)