x = input().split(" ")
if int(x[2]) - int(x[4]) >= 0 and int(x[3]) - int(x[4]) >= 0 and int(x[2]) + int(x[4]) <= int(x[0]) and int(x[3]) + int(x[4]) <= int(x[1]) :
    print("Yes")
else:
    print("No")
