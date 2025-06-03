ans = 0
while True:
    num = list(map(str,input().split()))
    if(num[1] == "?"): break
    a = int(num[0])
    b = int(num[2])
    op = num[1]
    if(op == "+"): ans=a+b
    elif(op == "-"): ans=a-b
    elif(op == "*"): ans=a*b
    elif(op == "/"): ans=a/b
    
    print("%d" %ans)
