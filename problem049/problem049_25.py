while True:
    h, w = map(int, raw_input().split())
    if (h == 0) & (w == 0):
        break
    line = ""
    for j in range(w):
        line += "#"
    for i in range(h):
        print line
    print ""