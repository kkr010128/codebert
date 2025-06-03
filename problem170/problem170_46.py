n,k=map(int,input().split())
DIV = 10**9+7

count = 0
for i in range(k,n+2):
  min_k = i*(i-1)/2
  max_k = i*(2*n-i+1)/2
  count += max_k - min_k + 1
print(int(count % DIV))