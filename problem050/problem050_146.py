def print_frame(h,w):
    if h == 1:
        print("#"*w)
        return
        
    if h == 2:
        print("#"*w)
        print("#"*w)
        return

    print("#"*w)
    for i in range(h-2):
        print("#",end="")
        for j in range(w-2):
           print(".",end="")
        print("#")
    print("#"*w)

while True:
    h,w = map(int,input().split())
    if h == 0 and w == 0:
        break;
    else :
        print_frame(h,w)
        print()