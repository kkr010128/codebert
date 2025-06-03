x = input()
x = x.split(" ")

width = int(x[0])
height = int(x[1])

area = width * height
perimeter = width * 2 + height * 2

print("{0} {1}".format(area, perimeter))