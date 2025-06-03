x, y, z = input().split()

# print(x, y, z)

# print("shuffle")
c = x
x = y
y = c
# print(1, "回目", x, y, z)
c = x
x = z
z = c
# print(2, "回目", x, y, z)

# print("result")
print(x, y, z)

