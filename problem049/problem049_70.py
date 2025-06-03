#coding:utf-8
#????????¢?????????

def draw_square(h, w):
    for i in range(h):
        a = ""
        for j in range(w):
            a += "#"
        print a

while 1:
    HW = raw_input().split()
    H = int(HW[0])
    W = int(HW[1])

    if H == 0 and W == 0:
        break

    draw_square(H, W)
    print ""