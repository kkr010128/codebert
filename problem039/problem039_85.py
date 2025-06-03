import sys


for line in sys.stdin:
    nums = list(map(int, line.split()))
    res = "Yes" if nums[0] < nums[1] < nums[2] else "No"
    print(res)

