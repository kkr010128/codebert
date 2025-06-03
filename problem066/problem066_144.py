while True:
    x=input()
    if x=="-":
        break
    else:
        m=int(input())
        for i in range(m):
            h=int(input())
            a=x[:h]
            b=x[h:]
            x=b+a
    print(x)
