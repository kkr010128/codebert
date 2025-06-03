def testfunc(start,end,target):
    cnt=0
    for num in range(start,end+1):
        if target % num ==0:
            cnt+=1
    print(cnt)

tmp=list(map(int,input().split()))
testfunc(tmp[0],tmp[1],tmp[2])
