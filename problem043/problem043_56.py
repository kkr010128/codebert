while True:
    n = map(int, raw_input().split())
    if (n[0] == 0) & (n[1] == 0):
        break
    print "%d %d" % (min(n), max(n))