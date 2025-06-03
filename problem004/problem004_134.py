import sys

for line in range(int(input())):
    str = input().split(" ")
    nums = sorted([int(str[2]), int(str[1]), int(str[0])])
    if nums[2]*nums[2] == nums[1]*nums[1] + nums[0]*nums[0]:
        print("YES")
    else:
        print("NO")