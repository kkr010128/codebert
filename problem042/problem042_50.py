def aizu005():
    cnt = 0
    while True:
        cnt =cnt + 1
        x = int(raw_input())
        if x == 0 :
            break
        else :
            print "Case " + str(cnt) + ": " + str(x)
aizu005()