N=int(input())
 
div = [0] * (N+1)
for d in range(1, N+1):
  for n in range(d, N, d):
      div[n] += 1
 
ans = sum(div[:N])
print(ans)