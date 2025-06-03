def resolve():
    x = int(input())
    t = 0
    pos = 100
    while True:
        pos += pos // 100
        # print(t, pos)
        t += 1
        if pos >= x:
            break
    print(t)

resolve()