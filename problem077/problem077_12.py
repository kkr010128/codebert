inputs = input().split(" ")
a = int(inputs[0])
b = int(inputs[1])
c = int(inputs[2])
d = int(inputs[3])

values = [a*c, a*d, b*c, b*d]
print(max(values))