import math

while True:
    n = int(input())
    if n == 0 :
        break
    nums = [int(x) for x in input().split(" ")]
    mean = sum(nums) / n

    variance = sum([(x - mean) ** 2 for x in nums]) / n
    std = math.sqrt(variance)
    print(std)