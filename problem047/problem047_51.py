while True:
    a,b,c = input().split()
    if b=='?':
        break
    elif b =='+':
        d = int(a) + int(c)
    elif b=='-':
        d = int(a) - int(c)
    elif b=='*':
        d = int(a)*int(c)
    else :
        d = int(a)/int(c)
    print(int(d))