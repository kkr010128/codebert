while True:
    m,f,r = map(int, input().split())
    if(m==-1 or f == -1):
        if (m == -1 and f == -1 and r == -1):
            break
        else:
            print('F')
    else:
        score = m + f
        if(score >= 80):
            print('A')
        elif(score >= 65):
            print('B')
        elif(score >= 50):
            print('C')
        elif(score >= 30):
            if(r >= 50):
                print('C')
            else:
                print('D')
        else:
            print('F')
