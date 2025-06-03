if __name__ == "__main__":
    i = 0
    while True:
        v = int(raw_input())
        if v == 0:
            break
        i += 1
        print "Case {0}: {1}".format(i,v)