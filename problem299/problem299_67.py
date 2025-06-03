N = int(input())
S = list(map(int,input().split()))
m = [0 for _ in range(N)]
for i in range(N):
  m[S[i]-1] = i+1
print(*m,sep=" ")
