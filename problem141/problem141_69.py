
N=int(input())
A=list(map(int,input().split()))
sum_value = sum(A)
chiled_value = 1
top_value = 1
if(N==0 and A[0]==1):
    print(1)
    exit()
if(A[0]!=0):
    print(-1)
    exit()
for i in range(1,N):
    if(sum_value >= chiled_value*2):
        top_value += chiled_value*2
        chiled_value = chiled_value*2-A[i]
        sum_value=sum_value-A[i]
        if(A[i+1]>chiled_value*2):
            print(-1)
            exit()
    elif(sum_value < chiled_value*2):
        chiled_value=sum_value
        top_value += chiled_value
        sum_value=sum_value-A[i]
    if(A[i]>=2**i):
        print(-1)
        exit()
if((sum_value-A[N])!=0):
    print(-1)
    exit()
print(top_value+A[N])



