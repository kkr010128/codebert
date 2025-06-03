nums = input().split()
a = int(nums[0])
b = int(nums[1])
c = int(nums[2])
if a < b < c:
    print('Yes')
elif a < c < b:
    print('No')
elif b < a < c:
    print('No')
elif b < c < a:
    print('No')
elif c < a < b:
    print('No')
else:
    print('No')