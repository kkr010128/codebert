x = input()
y = x.split(" ")
y = [int(z) for z in y]
w = y[0]
h = y[1]
x = y[2]
r = y[4]
y = y[3]
if (x <= w-r and x >= r) and (y <= h-r and y >= r):
    print("Yes")
else:
    print("No")