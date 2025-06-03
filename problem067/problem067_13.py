while True:
    try:
        a = int(input())
        t=0
        h=0
        for i in range(a):
            b,c=input().split()
            if b>c:
                t+=3
            elif c>b:
                h+=3
            else:
                t+=1
                h+=1
        print(t,h)
    except EOFError:break
