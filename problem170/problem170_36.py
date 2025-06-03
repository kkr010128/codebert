n,k = map(int, input().split())

ans = 0
for i in range(k, n + 2):
  min = i*(0+i-1)/2
  max = i*((n-i)+(n+1))/2
  ans += max - min +1
  
print(int(ans % (10**9 + 7)))