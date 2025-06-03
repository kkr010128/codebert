N = int(input())
nums = list(map(int,input().split()))

count = 0
current_max = nums[0]
for i in range(len(nums)-1):
    nv = nums[i+1]
    if nv > current_max:
        current_max = nv
    else:
        count += (current_max - nv)

print(count)