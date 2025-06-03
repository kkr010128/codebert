x = input()
y = x.split(" ")
y[0] = int(y[0])
y[1] = int(y[1])
if y[0] < y[1]:
    print("a < b")
elif y[0] > y[1]:
    print("a > b")
else:
    print("a == b")