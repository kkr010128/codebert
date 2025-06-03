num = int(input())
nums = input().split()

zero_flag = False
for item in nums:
  if item == '0':
    zero_flag = True
    break
    
if zero_flag:
  seki = 0
else:
  seki = 1
  for item in nums:
    seki *= int(item)
    if seki > 10**18:
      seki = -1
      break

print(seki)