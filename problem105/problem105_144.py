N=int(input())
A = list(map(int, input().split()))
c=0
for i in range(0,len(A),2):
  if A[i]%2==1:
    c+=1
print(c)