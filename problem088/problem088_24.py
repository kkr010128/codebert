n = int(input())
lis = list(map(int,input().split()))
sum = 0
for i in range(n-1):
  if int(lis[i])>int(lis[i+1]):
    sum += lis[i]-lis[i+1]
    lis[i+1] = lis[i]
  else:
    continue
print(sum)