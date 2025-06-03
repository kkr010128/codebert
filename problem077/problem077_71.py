nums = [int(e) for e in input().split()]
a=nums[0]
b=nums[1]
c=nums[2]
d=nums[3]
max = a*c
if a * d > max:
    max = a * d
if b * c > max:
    max = b * c
if b * d > max:
    max = b * d

print(max)