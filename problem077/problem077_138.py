N = input()
num = N.split(' ')
a = int(num[0])
b = int(num[1])
c = int(num[2])
d = int(num[3])

e = a * c
f = a * d
g = b * c
h = b * d
num_max = max([e, f, g, h])
print(num_max)