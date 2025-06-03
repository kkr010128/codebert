N,K = map(int,input().split())
count = 0
for i in range(K,N+2):
  min_1 = i*(i-1)//2
  max_1 = (2*N-i+1)*i//2
  num = max_1-min_1+1
  count += num
print(count%(10**9+7))