def chess(h,w):
    o = ""
    for i in range(h):
        if i%2:
            if w%2: o+= ".#"*(w/2)+".\n"
            else: o+= ".#"*(w/2)+"\n"
        else:
            if w%2: o+= "#."*(w/2)+"#\n"
            else: o+= "#."*(w/2)+"\n"
    print o

while 1:
    h,w=map(int,raw_input().split())
    if h==w==0:break
    chess(h,w)