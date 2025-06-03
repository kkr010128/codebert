while True:
    num = list(map(int,input().split()))
    if(num[0] == 0 and num[1] == 0): break
    c = 0
    for i in range(1,num[0] - 1):
        for j in range(i+1,num[0]):
            for k in range(j+1,num[0]+1):
                if(i+j+k == num[1]): c += 1
    
    print(c)
