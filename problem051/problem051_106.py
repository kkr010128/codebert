while True:
    s=input().split()
    h=int(s[0])
    w=int(s[1])
    if h==0:
        break
    for i in range(1,h+1):
        if i%2==1:
            if w%2==0:
                print("#."*(w//2))
            else:
                print("#."*(w//2)+"#")
        else:
            if w%2==0:
                print(".#"*(w//2))
            else:
                print(".#"*(w//2)+".")
    print()
