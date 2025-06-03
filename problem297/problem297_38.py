import math

n = int(input())

answer = (n - math.floor(n / 2)) / n

print(answer)

# nums = list(range(1, n + 1))
# 
# odds = [x for x in nums if x % 2 == 1]
# 
# if len(nums) % 2 == 0:
#     print(0.5)
# else:
#     print(len(odds) / len(nums))
