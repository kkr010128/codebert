while True:
    L = raw_input().split()

    a = int(L[0])
    o = (L[1])
    b = int(L[2])

    if o == "?":
         break
        
    elif o == "+":
        print a + b
    elif o == "-":
        print a - b
    elif o == "*":
        print a * b
    elif o == "/":
        print a/b