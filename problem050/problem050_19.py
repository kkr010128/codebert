while True:
    h,w = map(int,raw_input().split())
    if h == w == 0:break
    print ("#" * w)
    print (("#" + "." * (w - 2) + "#" + "\n") * (h - 3))+("#" + "." *(w-2)+"#")
    print ("#" * w + "\n")