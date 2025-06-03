#coding:utf-8
#?????§?????????????????????

def draw_odd(n):
    a = ""
    for i in range(n/2):
        a += "#."
    if n % 2 != 0:
        a += "#"
    print a

def draw_even(n):
    a = ""
    for i in range(n/2):
        a += ".#"
    if n % 2 != 0:
        a += "."
    print a

while 1:
    HW = raw_input().split()
    H = int(HW[0])
    W = int(HW[1])

    if H == 0 and W == 0:
        break

    for i in range(H/2):
        draw_odd(W)
        draw_even(W)
    if H % 2 != 0:
        draw_odd(W)
    print ""