while(True):
    input = raw_input().split()
    a = int(input[0])
    b = int(input[2])
    if input[1] == "?":
        break
    elif input[1] == "+":
        print a + b
    elif input[1] == "-":
        print a - b
    elif input[1] == "*":
        print a * b
    elif input[1] == "/":
        print a / b