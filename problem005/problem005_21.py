while True:
    try:
        r = sorted(list(map(int, input().split())))
        
        
        def euclidfunc(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        
        def lcmfunc(a, b):
            return a * b // euclidfunc(a, b)
        
        
        print("{a} {b}".format(a=euclidfunc(r[1], r[0]), b=lcmfunc(r[1], r[0])))
    except EOFError:
        break

