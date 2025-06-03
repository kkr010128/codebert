#coding:utf-8

while True:
    h, w = map(int, raw_input().split())
    if h == w == 0:
        break
    print(w * "#")
    for i in xrange(h - 2):
        print("#" +"." *(w - 2) +"#")
    print(w * "#")
    print("")