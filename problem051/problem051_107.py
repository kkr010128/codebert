while True:
    L = map(int,raw_input().split())
    H = (L[0])
    W = (L[1])
    
    if H == 0 and W == 0:break
    for x in range(0,H):
        if x % 2 == 0:
            if W % 2 == 1:
                print "{}#".format("#."* (W / 2))
            else:
                print "#." * (W / 2)
        else:
            if W % 2 == 1:
                print "{}.".format(".#"* (W / 2))
            else:
                print ".#" * (W / 2)

    print ""