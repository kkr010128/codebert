def az10():
    while True:
        xs = raw_input().split()
        a,op,b = int(xs[0]),xs[1],int(xs[2])
        if op == "?" : break
        if op == "+" : print (a + b)
        if op == "-" : print (a - b)
        if op == "*" : print (a * b)
        if op == "/" : print (a / b)

az10()