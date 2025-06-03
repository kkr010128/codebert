n = int(input())
nums = input().split()
max = int(nums[0])
min = int(nums[0])
sum = int(nums[0])
for i in range(n-1):
    m = int(nums[i+1])
    if m > max:
        max = m
    if m < min:
        min = m
    sum = sum + m
    
print(min, max, sum)