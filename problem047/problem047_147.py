ans = 0
while True:
    x = input()
    x = x.split(" ")
    if x[1] == "?": break
    if x[1] == "+":
        ans = int(x[0]) + int(x[2])
    elif x[1] == "-":
        ans = int(x[0]) - int(x[2])
    elif x[1] == "*":
        ans = int(x[0]) * int(x[2])
    elif x[1] == "/":
        ans = int(x[0]) / int(x[2])
    print("%d" % ans)