N=int(input())
*A,=map(int,input().split())
T=[0]*N
for i in range(N):
 T[~-A[i]]=i+1
print(*T)