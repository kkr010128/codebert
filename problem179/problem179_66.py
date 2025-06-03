N,M = map(int,input().split())
A_ls = list(map(int,input().split()))

cnt = 0
vote = sum(A_ls) / (4 * M)
for i in range(N):
  if A_ls[i] >= vote:
    cnt += 1
    
print("Yes" if cnt >= M else "No")