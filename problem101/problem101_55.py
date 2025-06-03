main=list(map(int,input().split()))
k=int(input())
for i in range(k):
    if(main[0]>=main[1]):
        main[1]=main[1]*2
    elif(main[1]>=main[2]):
        main[2]=main[2]*2
if(main[1]>main[0] and main[2]>main[1]): print('Yes')
else: print('No')