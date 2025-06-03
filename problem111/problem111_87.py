n=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
q=[]
for i in range(n):
  if i==0:
    q.append(A[i])
  else:
    q+=[A[i]]*2
print(sum(q[:n-1]))