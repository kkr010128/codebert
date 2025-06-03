l=raw_input()
k=l.split()
H=int(k[0])
W=int(k[1])
while True:
        if H+W==0:
                break
        else:
                for i in range(H):
                        print "#"*W
                print ""
                l=raw_input()
                k=l.split()
                H=int(k[0])
                W=int(k[1])