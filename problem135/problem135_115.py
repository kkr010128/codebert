nums = input().split()

a = int(nums[0])
b = int(nums[1].replace('.', ''))

result = str(a * b)
if len(result) < 3:
  print(0)
else:
  print(result[:-2])