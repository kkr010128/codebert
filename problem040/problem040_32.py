a, b, c = raw_input().split()

def ITP1(a, b, c):
    if (a <= b):
        if (b <= c):
            print a, b, c
            return
        if (c <= b):
            if (c <= a):
                print c, a, b
                return
            if (a <= c):
                print a, c, b
                return
    if (b <= a):
        if (a <= c):
            print b, a, c
            return
        if (c <= a):
            if (c <= b):
                print c, b, a
                return
            if (b <= c):
                print b, c, a
                return

ITP1(a, b, c)