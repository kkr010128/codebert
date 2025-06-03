while 1:
    h,w=map(int,input().split())
    if h==0 and w==0: break
    for y in range(h): print(('#.'*w)[y % 2:][:w])
    print('')