line = input()
words = line.split()
nums = list(map(int, words))
a = nums[0]
b = nums[1]

d = a // b
r = a % b
f = a / b
f = round(f,5)

print ("{0} {1} {2}".format(d,r,f))