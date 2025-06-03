import sys

while(1):
    H, W = map(int, raw_input().split())
    if(H == 0 and W == 0):
        break
    else:
        for i in range(H):
            for j in range(W):
                if(i%2==0 and j%2==0):
                    sys.stdout.write("#")
                elif(i%2==0 and j%2==1):
                    sys.stdout.write(".")
                elif(i%2==1 and j%2==0):
                    sys.stdout.write(".")
                else:
                    sys.stdout.write("#")
            print
        print