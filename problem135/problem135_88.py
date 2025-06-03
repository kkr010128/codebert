a, b = input().split()
a = int(a)
b = str(b).replace(".", "")
x = a * int(b)
if x < 100:
    print(0)
else:
    print(str(x)[:-2])
