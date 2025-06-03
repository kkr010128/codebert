nums = list(input().split())
for i, j in enumerate(nums):
    if j == '0':
        print(i+1)