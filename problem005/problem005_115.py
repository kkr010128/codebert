while True:
    try:
        # a >=b
        a, b = sorted(map(int, input().strip("\n").split(" ")), reverse=True)
        d = a * b

        # calc. gcm by　ユークリッド互除法
        while True:
            c = a % b
            # print("{0} {1} {2}".format(a, b, c))
            if c == 0:
                break
            else:
                a, b = sorted([b, a % b], reverse=True)
        gcm = b
        lcm = d / gcm
        # print("gcm is {}".format(b))
        print("{0:d} {1:d}".format(int(gcm), int(lcm)))

        #print("{0} {1}".format(a, b))
        #a, b = sorted([b, a % b], reverse=True)
        #print("{0} {1}".format(a, b))

    except EOFError:
        break  # escape from while loop