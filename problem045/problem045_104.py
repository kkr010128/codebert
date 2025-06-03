nums = list(map(int , input().split()))
a = nums[0]
b = nums[1]
print(a // b , end = " ")
print(a % b , end = " ")
print("{0:.5f}".format((a / b)))