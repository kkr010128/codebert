n = int(input())
a = list(map(int,input().split()))
b = [0]*n
for i in range(n):
  b[i] = a[i] + b[i-1]
ans = b[-1]
for j in range(n):
  ans = min(ans,abs(b[-1]-b[j]*2))
print(ans)