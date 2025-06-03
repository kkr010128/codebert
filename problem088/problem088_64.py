N = int(input())
As = list(map(int, input().split()))

height = 1
step = 0

for i in range(N):
  if As[i] < height:
    step += height - As[i]
  else:
    height = As[i]
    
print(step)