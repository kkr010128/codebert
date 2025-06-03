import math
alpha = []
while True:
    n = float(raw_input())
    if n == 0:
        break
    nums_str = raw_input().split()
    nums = []
    for s in nums_str:
        nums.append(float(s))
    ave = sum(nums)/n
    n_sum = 0.0
    for num in nums:
        n_sum += (num-ave)**2
    alpha.append(n_sum/n)
for a in alpha:
    print math.sqrt(a)