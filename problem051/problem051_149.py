import sys
for i in sys.stdin.readlines(): 
    nums = list(map(int,i.split()))
    h = nums[0]
    w = nums[1]
    if h == 0 and w == 0:
        break
    for j in range(1,h+1):
        if h == 1 and w == 1:
            print("#")
        elif j % 2 == 1:
            if w % 2 == 1:
                x = int((w-1)/2)
                print("#."*x +"#")
            else:
                x = int(w/2)
                print("#."*x)
        elif j % 2 == 0:
            if w % 2 == 1:
                x = int((w-1)/2)
                print(".#"*x +".")
            else:
                x = int(w/2)
                print(".#"*x)
    print("")