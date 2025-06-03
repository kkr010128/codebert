while(True):
        h,w = [int(i) for i in input().split()]
        if h == 0 and w == 0:
                break
        for i in range(h):
                out = ''
                for j in range(w):
                        if j == 0 or j == (w-1) or i == 0 or i == (h-1):
                                out += '#'
                        else :
                                out += '.'
                print(out)
        print('')