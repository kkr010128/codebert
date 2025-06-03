while True:
    h, w =map(int,input().split())
    odd = '#.'*300
    even = '.#'*300
    if h == 0 and w==0:
        break
    for i in range(h):
        if i%2 ==0:
            out = odd[:w]
        else:  
            out= even[:w]
        print(out)
    print()