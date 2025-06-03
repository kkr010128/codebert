judge = True

while judge:
    h,w = map(int, input().split(" "))
    if h == 0 and w == 0:
        judge = False
    else:
        for i in range(h):
            if i == 0 or i+1 == h:
                print("#"*w)
            else:
                print("#"+"."*(w-2)+"#")
        print()