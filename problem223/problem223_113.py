N, K = map(int, input().split())
p = list(map(int, input().split()))
tmp = sum(p[:K]) 
maxsum = tmp
#print(p[:K])
for i in range(1,N-K+1):
  #print(p[i:i+K])
  tmp = tmp - p[i-1] + p[i+K-1]
  maxsum = max(maxsum, tmp)
ans = (maxsum + K) / 2
print(ans)