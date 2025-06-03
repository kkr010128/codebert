X=int(input())
while True:
    flg = True
    for i in range(2,int(X**1/2)+1):
        if X%i == 0:
            flg = False
            break
    if flg == True:
        print(X)
        break
    else:
        X += 1
