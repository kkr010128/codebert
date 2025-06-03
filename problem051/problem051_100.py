while True :
    H, W = map(int, raw_input().split(" "))
    if (H == W == 0) :
        break
    ans = ""
    for h in range(0, H) :
        for w in range(0, W) :
            if ((w + h) % 2 == 0) :
                ans += "#"
            else :
                ans += "."
        ans += "\n"
    print("%s" % (ans))