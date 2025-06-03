N = int(input())
X = list(map(int,input().split()))
ans = []
for i in range(max(X)):
  P = i+1
  sum = 0
  for j in range(N):
    sum += (X[j]-P)**2
  ans.append(sum)

print(min(ans))