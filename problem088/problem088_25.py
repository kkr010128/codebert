N = int(input())
S = list(map(int,input().split()))

ans = 0
for i in range(N-1):
  add = max(S[i] - S[i+1],0)
  S[i+1] += add
  ans += add
  
print(ans)
