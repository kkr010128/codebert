while True:
    string = input()
    if string == "-":
        break
    else:
        s = 0
        for i in range(int(input())):
            s += int(input())

        s = s % len(string)
    print(string[s:len(string)] + string[0:s])