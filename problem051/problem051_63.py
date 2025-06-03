while True:
    a=[int(x) for x in input().split()]
    if a[0]==a[1]==0:
        break
    else:
        for x in range(a[0]):
            if x%2!=0:
                for y in range(a[1]):
                    if y%2!=0:
                        print("#", end="")
                    else:
                        print(".", end="")
                print("\n",end="")
            elif x%2==0:
                for y in range(a[1]):
                    if y%2!=0:
                        print(".", end="")
                    else:
                        print("#", end="")
                print("\n",end="")
    print("")