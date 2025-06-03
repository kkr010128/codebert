N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(N):
  for j in range(i+1,N):
    temp = A[i]*A[j]
    ans += temp
print(ans)