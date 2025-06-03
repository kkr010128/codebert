def aizu006():
    while True:
        xs = map(int,raw_input().split())
        if xs[0] == 0 and xs[1] == 0: break
        else:
            xs.sort()
            for i in range(0,2):
                print xs[i],
            print
aizu006()