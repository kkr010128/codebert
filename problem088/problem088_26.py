n = int(input())
heights = list(map(int, input().split()))
cnt = 0
for i in range(1,n):
  if heights[i] >= heights[i-1]:
    pass
  else:
    x = heights[i-1] - heights[i]
    cnt += x
    heights[i] = heights[i-1]
    
print(cnt)