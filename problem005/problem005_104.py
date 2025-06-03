while(1):
    try:
        i = raw_input()
        a, b = map(int, i.split())
        x, y = a, b
        while(b != 0):
            tmp = b
            b = a % b
            a = tmp
        print a,
        print x*y/a
    except:
        break