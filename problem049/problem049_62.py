while True:
    h,w = map(int, raw_input().split())
    if h == w == 0:
        break
    print (("#" * w + "\n") * h)