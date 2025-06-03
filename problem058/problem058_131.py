while True:
    max,sum=map(int,input().split())
    if max==0 and sum==0:
        break
    cnt=0
    for i in range(1,max+1):
        for j in range(i+1,max+1):
            for k in range(j+1,max+1):
                if i+j+k==sum:
                    cnt+=1
    print(cnt)