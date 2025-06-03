#coding:utf-8

while True:
    try:
        a, b = map(int, raw_input(). split())
        x = a * b
        while True:
            c = a % b
            a = b
            b = c
            if b == 0:
                break
        x = x / a
        print("%d %d" % (a, x))
    except:
        break