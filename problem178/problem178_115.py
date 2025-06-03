x,y,z = map(int, input().split())
x = x^y
y = x^y
x = x^y
x = z^x
z = z^x
x = z^x
print("{} {} {}".format(x,y,z))