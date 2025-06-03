string = input()
numbers = string.split()
a, b = int(numbers[0]), int(numbers[1])
d = a//b
r = a%b
f = a/b
print(d, r, "{:.12f}".format(f))
