while True:
    s=input().split()
    t=[int(i) for i in s]
    H=t[0]
    W=t[1]
    if H==0:
        break
    else:
        print("#"*W)
        for i in range(H-2):
            print("#"+"."*(W-2)+"#")
        print("#"*W)
        print()
