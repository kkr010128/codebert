
x = input()

split_x = x.split(sep=" ")

a = split_x[0]
b = split_x[1]

if int(a) < int(b):
    print("a < b")

if int(a) == int(b):
    print("a == b")

if int(a) > int(b):
    print("a > b")