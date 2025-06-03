while True:
    num = map(int, raw_input().split())
    num.sort()
    if num[0] == 0 and num[1] == 0:
        break
    print "%d %d" % (num[0], num[1])