while True:
    h,w=map(int,input().split())
    if h==0 and w==0:
        break
    for y in range(h):
        cnt=y%2
        for x in range(w):
            if cnt==0:
                if x%2==0:
                    print("#",end='')
                else:
                    print(".",end='')
            else:
                if x%2==0:
                    print(".",end='')
                else:
                    print("#",end='')
        print()
    print()