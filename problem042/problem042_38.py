array = []
x = input()
while x != "0":
    array.append(x)
    x = input()
for i, x in enumerate(array):
    print("Case %d: %s" % (i + 1, x))
