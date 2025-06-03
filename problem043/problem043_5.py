while 1:
    tmp = map(int, raw_input().split())
    if tmp[0] == tmp[1] == 0:
        break
    else:
        print " ".join(map(str, sorted(tmp)))
