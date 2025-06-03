input_line = input()
l = input_line.split()
if int(l[0]) < int(l[1]):
    print("a < b")
elif int(l[0]) > int(l[1]):
    print("a > b")
else:
    print("a == b")