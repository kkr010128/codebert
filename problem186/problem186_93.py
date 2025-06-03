K, N = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
ans = 0
del_A = []
for i in range(N):
  if(i==(N-1)):
    del_A.append(A[0]+K-A[i])
  else:
    del_A.append(A[i+1]-A[i])
print(sum(del_A)-max(del_A))