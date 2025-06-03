while True:
    a,op,b = input().split()
    a = int(a)
    b = int(b)
    if op == "?":
        break
    else:
        if op == "+":
            ans = a + b
        elif op == "-":
            ans = a-b
        elif op == "*":
            ans = a * b
        elif op == "/":
            rem = a%b
            if rem == 0:
                ans = int(a/b)
            else:
                ans = int(a/b)
    print(ans)  
    
