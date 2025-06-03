while True:
    l = map(int, raw_input().split())
    num = map(int, raw_input().split())
    print "%d %d %d" % (min(num),max(num),sum(num))
    break