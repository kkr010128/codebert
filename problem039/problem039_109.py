input_line = input()
l = input_line.split()
if int(l[0]) < int(l[1]) < int(l[2]):
    print("Yes")
else:
    print("No")