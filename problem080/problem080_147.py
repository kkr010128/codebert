N=int(input())
A,B=[],[]
for i in range(N):
  x,y=map(int, input().split())
  A.append(x+y)
  B.append(x-y)
  
A=sorted(A)
B=sorted(B)
print(max(abs(A[0]-A[-1]),abs(B[0]-B[-1])))