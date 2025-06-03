while True:
    inVal = input().split()
    if inVal[1] == "?":
        break
    if inVal[1] == "+":
        print(int(inVal[0]) + int(inVal[2]))
    elif inVal[1] == "-":
        print(int(inVal[0]) - int(inVal[2]))
    elif inVal[1] == "*":
        print(int(inVal[0]) * int(inVal[2]))
    elif inVal[1] == "/":
        print(int(inVal[0]) // int(inVal[2]))
