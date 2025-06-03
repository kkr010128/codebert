S=input()
if S=="SSS":
    print(0)
else:
    if S=="RSS" or S=="SRS":
        print(1)
    else:
        if S=="SSR" or S=="RSR":
            print(1)
        else:
            if S=="RRS" or S=="SRR":
                print(2)
            else:
                print(3)