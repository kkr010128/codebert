
nums = []

while True:
    num = [int(e) for e in input().split()]
    if num[0]==0 and num[1]==0:
        break
    nums.append(num)

for i in range(len(nums)):
    for j in range(len(nums[i])):
        for k in range(j):
            if nums[i][k] > nums[i][j]:
                a = nums[i][k]
                nums[i][k] = nums[i][j]
                nums[i][j] = a

for i in range(len(nums)):
    print(" ".join(map(str, nums[i])))
