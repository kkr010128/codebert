N=int(input())
A=list(map(int,input().split()))
count=0
for i in range(len(A)):
  if A[i]%2==0:
    if A[i]%3==0 or A[i]%5==0:
      count+=1
  else:
    count+=1
if count==len(A):
  print("APPROVED")
else:
  print("DENIED")