nums = list(map(int,input().split()))
N = nums[0]
M = nums[1]
numss = list(map(int,input().split()))
cnt = M
summ = sum(numss)
for num in numss:
  if num >= summ/(M*4):
    cnt -= 1
if cnt > 0:
  print("No")
else:
  print("Yes")