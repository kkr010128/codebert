while 1:
    H,W=[int(i) for i in input().split()]
    if H==W==0:
        break
    else:
        if W<=2:
            for i in range(H):
                for s in range (W):
                    print("#",end="")
                print('')
            print('')
        else:
            for s in range(W):
                print("#",end="")
            print('')
            for i in range(H-2):
                print('#',end="")
                for s in range (W-2):
                    print(".",end="")
                print('#',end="")
                print('')
            for s in range(W):
                print("#",end="")
            print('')
        print('')