while True:
    h,w=map(int,input().split())
    if h==0 and w==0:
        break
    for y in range(h):
        for x in range(w):
            if y==0 or y==h-1 or x==0 or x==w-1:
                print("#",end='')
            else:
                print(".",end='')
        print()
    print()