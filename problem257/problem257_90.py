N=int(input())
L=list(map(int,input().split()))
i=0
n=1
while True:
  if i==N:
    break
  if L[i]==n:
    n+=1
  i+=1
if n==1:
  print(-1)
else:
  print(N-n+1)