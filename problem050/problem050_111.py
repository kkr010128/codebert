#coding:utf-8
#?????¬???????????????

def draw_topbottom(n):
    a = ""
    for i in range(n):
        a += "#"
    print a

def draw_middle(n):
    a = "#"
    for i in range(n-2):
        a += "."
    a += "#"
    print a

while 1:
    HW = raw_input().split()
    H = int(HW[0])
    W = int(HW[1])

    if H == 0 and W == 0:
        break

    draw_topbottom(W)
    for i in range(H-2):
        draw_middle(W)
    draw_topbottom(W)
    print ""