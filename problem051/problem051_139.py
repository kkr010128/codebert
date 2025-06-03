while True:
    h, w = map(int, raw_input().split())
    if (h == 0) & (w == 0):
        break
    line0 = ""
    line1 = "."
    for i in range(w):
        if i % 2 == 0:
            line0 += "#"
        else:
            line0 += "."
    line1 += line0[:-1]

    for j in range(h):
        if j % 2 == 0:
            print line0
        else:
            print line1
    print ""