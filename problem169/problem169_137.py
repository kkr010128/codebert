N = int(input())
L = list(map(int,input().split()))
ans = [0 for i in range(N)]
for i in range(len(L)):
  ans[L[i]-1] += 1
for i in range(N):
  print(ans[i])