def az8():
    xs = map(int,raw_input().split())
    a,b = xs[0],xs[1]
    print (a/b),(a%b), "%5f"%(float(a)/b)
az8()