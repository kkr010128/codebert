N = input()
nums = []

for num in N:
    nums.append(int(num))

s = sum(nums)
if s % 9 == 0:
    print("Yes")
else:
    print("No")
