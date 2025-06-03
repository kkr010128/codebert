N = int(input())
cc = list(map(int,input().split()))
min_sum = float('inf')
for i in range(1,101):
  count = 0
  for j in cc:
    count += (i-j)**2
  min_sum = min(min_sum,count)
print(min_sum)