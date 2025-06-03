while True:
    [a,b,c]=[x for x in input().split()]
    [a,c]=[int(a),int(c)]
    op=b
    if op=="?":
        break
    elif op=="+":
        print(a+c)
    elif op=="-":
        print(a-c)
    elif op=="*":
        print(a*c)
    else:
        print(a//c)