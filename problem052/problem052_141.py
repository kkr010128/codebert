def modz( x, n):
    a = x / n
    return x - a*n

if __name__ == "__main__":

    n = int(raw_input())

    s = ""
    i = 1

    while True:
        # print "i:{0}".format(i)
        x = i;
        if modz(x , 3) == 0:
            s += " " + str(i)
        else:
            ex = 0
            while True:
                if modz(x , 10) == 3:
                    s += " " + str(i)
                    ex = 1
                    break
                x /= 10
                if x == 0:
                    ex = 1
                    break

        if (i+1) > n:
            i += 1
            break
        i += 1

    print s