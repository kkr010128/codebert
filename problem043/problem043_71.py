while True:
    num = list(map(int,input().split()))
    if(num[0] == 0 and num[1] == 0):
        break
    else:
        if(num[0] > num[1]):
            print("%d %d" %(num[1],num[0]))
        else:
            print("%d %d" %(num[0],num[1]))
            
