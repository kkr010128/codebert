for i in range(1,int(input())+1):
    x=i
    if x % 3 == 0:
        print(" "+str(i), end="")
    else:
        while x != 0:
            if x % 10 == 3:
                print(" "+str(i), end="")
                break
            else:
                x = x//10
print("")