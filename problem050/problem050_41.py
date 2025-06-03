while True:
    h, w = map(int, raw_input().split())
    if h == 0 and w == 0:
        break
    print(("#" * w + "\n") + ("#" + "." * (w-2) + "#" + "\n") * (h-2) + ("#" * w + "\n"))