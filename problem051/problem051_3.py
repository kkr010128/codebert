while True:
    data = map(int, raw_input().split())
    if data[0] == 0 and data[1] == 0:
        break
    else:
        for i in range(data[0]):
            if i % 2 == 0:
                if data[1] % 2 == 0:
                    print "#." * (data[1] / 2)
                else :
                    print "#." * (data[1] / 2) + "#"
            elif i % 2 == 1:
                if data[1] % 2 == 0:
                    print ".#" * (data[1] / 2)
                else :
                    print ".#" * (data[1] / 2) + "."
        print 