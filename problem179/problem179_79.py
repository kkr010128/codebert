N, M = (int(x) for x in input().split())
A = list(map(int, input().split()))
sum=0
cnt=0
for i in range(N):
  sum+=A[i]
sum/=4*M
for i in range(N):
  if A[i]>=sum:
    cnt+=1
if cnt>=M:
  print("Yes")
else:
  print("No")