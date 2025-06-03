put = ['#','.']
while(True):
        h,w = [int(i) for i in input().split()]
        if h==0 and w==0:
                break
        for i in range(h):
                out = ''
                if i % 2 == 0:
                    count = 0
                else :
                    count = 1 
                for j in range(w):
                        out += put[count%2]
                        count += 1
                print(out)
        print("")