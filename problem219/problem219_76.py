s = input()
nums = list(reversed([int(c) for c in s])) + [0]
r = (0, 1) # no borrow, with borrow
for i in range(len(nums)):
    # print(r)
    next_no_borrow = min(r[0] + nums[i], r[1] + nums[i] + 1)
    next_borrow = min(10 - nums[i] + r[0], 9 - nums[i] + r[1])
    r = (next_no_borrow, next_borrow)
print(min(r))
