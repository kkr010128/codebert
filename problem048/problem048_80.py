input()
nums = [int(x) for x in input().split(" ")]
print("{0} {1} {2}".format(min(nums), max(nums), sum(nums)))