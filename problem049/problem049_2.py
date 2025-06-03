#coding:utf-8

while True:
    h, w = map(int, raw_input(). split())
    if h == w == 0:
        break
    for i in xrange(h):
        print("#" * w)
    print("")