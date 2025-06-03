nums = input().split()
a = int( nums[0])
b = int( nums[1])
c = int( nums[2])

if a > b:
    tmp = a
    a = b
    b = tmp
if b > c:
    tmp = b
    b = c
    c = tmp
if a > b:
    tmp = a
    a = b
    b = tmp

print( a, b, c)