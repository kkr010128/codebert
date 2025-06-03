while 1:
        i,j =map(int,raw_input().split())
        if i == j == 0:
                break
        elif 0<i<300 and 0<j<300:
                print (("#"*j + "\n")*i)