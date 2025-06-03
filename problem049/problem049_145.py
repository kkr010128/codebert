while 1 :
    try:
        h,w=map(int,input().split())
        #print(h,w)
        if( h==0 and w==0 ): 
            break
        else:
            for hi in range(h):
                print("#" * w)
            print() #??????
        if( h==0 and w==0 ): break
    except (EOFError):
        #print("EOFError")
        break