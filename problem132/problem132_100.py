N, K= map(int,input().split())
a = list(map(int,input().split()))
p=0
while p<K:
  B=[0]*(N+1)
  for i in range(N):
    t = a[i]
    B[max(i-t,0)] +=1
    B[min(i+t+1,N)] -=1
  for i in range(N):
    B[i+1] += B[i]
  a=B[:N]        
  if min(a)==N:
    break
  p+=1
print(*a)