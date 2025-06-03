num = input().split()
nums = []
for i in num:
  nums.append(int(i))
#print(nums)
price = [300000, 200000, 100000]
result = []
 
#2 3 4 5 6
for i in nums:
  if int(i) > 3:
    result.append(0)
  else:
    result.append(price[i-1])
value = result[0] + result[1]
if value == 600000:
  print("1000000")
else:
  print(value)