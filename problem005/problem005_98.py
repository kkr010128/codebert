while True:
    try:
        As,Bs = map(int,input().split())
        a,b = As, Bs
        while True:
            if a % b == 0:
                gcd = b
                break
            a,b = b, a % b
        print(gcd,int(As * Bs / gcd))
    except EOFError:
        break