while 1:

    string = raw_input()
    if string == "-":
        break

    l = len(string)

    for i in xrange(int(input())):

        h = int(input())

        lower  = string[0:h]
        upper  = string[h:l]

        string = upper + lower

    print string