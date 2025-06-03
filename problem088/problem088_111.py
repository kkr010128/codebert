n = int(input())
a = list(map(int, input().split()))
amax = a[0]
asum = 0
acount = 0
result = 0

for i in range(0,n):
  if amax > a[i]:
    acount+=1
    asum+=a[i]
    if i == n-1:
      result += amax*acount-asum
  else:
    result += amax*acount-asum
    amax = a[i]
    asum = 0
    acount = 0

    
print(result)