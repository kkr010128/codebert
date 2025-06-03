N=int(input())
A,B=map(str,input().split())
S=""
for i in range(N):
  S+=A[i]
  S+=B[i]
print(S)