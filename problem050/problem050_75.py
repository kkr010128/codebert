if __name__ == "__main__":
    while True:
        h,w = map(int,input().split())
        if w is not 0 or h is not 0:
            for i in range(w):
                print("#",end="")
            print("")
            for i in range(h-2):
                print("#",end="")
                for j in range(w-2):
                    print(".",end="")
                print("#",end="")
                print("")
            for i in range(w):
                print("#",end="")
            print("")   
            print("")
        else:
            break