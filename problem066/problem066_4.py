while(1):
    str = raw_input()
    if str == "-":
        break
    else:
        m = int(raw_input())
        for i in range(m):
            h = int(raw_input())
            str = str[h:len(str)] + str[0:h]
        print str