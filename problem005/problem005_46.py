while 1:
        try:
                a, b = map(int,raw_input().split())
        except EOFError:
                break
        ac, bc = a, b
        while 1:
                if a < b:
                        b = b - a
                elif b < a:
                        a = a - b
                elif a == b:
                        x = [a,ac*bc/a]
                        print "{:.10g} {:.10g}".format(*x)
                        break