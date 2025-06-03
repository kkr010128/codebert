import math
N=int(input())
A=[0]*N
B=[0]*N
for i in range(N):
	A[i],B[i]=map(int,input().split())
total=0
for i in range(N):
  for j in range(i+1,N):
    total+=((A[i]-A[j])**2+(B[i]-B[j])**2)**0.5
    
    

print(total/N*2)