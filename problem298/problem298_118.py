N,K=map(int,input().split())
h=list(map(int, input().split()))
A=0
for i in h:
  if i>=K:
    A=A+1
print(A)