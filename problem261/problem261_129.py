S = str(input())
n = len(S)
m = n//2
ans = 0
for i in range(m):
  if S[i] != S[-1-i]:
    ans +=1
print(ans)
