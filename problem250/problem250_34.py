import math
n = int(input())
while 1:
    flg=1
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            flg=0
            break
    if flg==1:
        print(n)
        break
    n+=1
