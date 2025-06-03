#D
N=int(input())
X=str(input())
   
CNT=0
for i in range(N):
    if X[i]=="1":
        CNT+=1
NUM=int(X,2)

to0_cnt=[0 for i in range(N)]
for i in range(1,N):
    ans=0
    num=i
    while True:
        cnt=0
        for j in bin(num)[2:]:
            if j=="1":
                cnt+=1
        if cnt==0:
            break
        r=num%cnt
        ans+=1
        if r==0:
            break
        num=r
    to0_cnt[i]=ans
                
R=[NUM%(CNT+1),NUM%(CNT-1) if CNT!=1 else 0]
for i in range(N):
    if X[i]=="0":
        cnt=CNT+1
        r=(R[0]+pow(2,N-i-1,cnt))%cnt
    else:
        cnt=CNT-1
        if NUM-pow(2,N-i-1)==0:
            print(0)
            continue
        r=(R[1]-pow(2,N-i-1,cnt))%cnt
    
    ans=1+to0_cnt[r]
    print(ans)