x = int(input())

nums = [True]*(10**6)
n = int(10**6**0.5)
for i in range(4, 10**6, 2): nums[i] = False
for i in range(3, n, 2):
  if nums[i]:
    for j in range(i+i, 10**6, i): nums[j] = False
      
while True:
  if nums[x]:
    print(x)
    break
  x += 1