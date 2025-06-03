s = input().split(" ")
nums = list(map(int, s))
if nums[0] > nums[1]:
    print("a > b")
elif nums[0] < nums[1]:
    print("a < b")
else:
    print("a == b")