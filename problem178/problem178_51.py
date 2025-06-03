combined = input().split(" ")
a = combined[0]
b = combined[1]
c = combined[2]

temp1 = b
b = a
a = temp1

temp2 = c
c = a
a = temp2

print(a, b, c)