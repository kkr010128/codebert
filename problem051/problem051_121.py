#coding:UTF-8
while True:
    h,w = map(int,raw_input().split())
    if h == 0 and w == 0:
        break
    for i in range(h):
        if i%2 == 1:
            if w % 2 == 0:
                print ".#" * (w / 2)
            else:
                print ".#" * (w / 2) + "."
        else:
            if w % 2 == 0:
                print "#." * (w/2)
            else:
                print "#." * (w/2) + "#"
    print ""