import sys
K=int(input())
if K%2==0 or K%5==0:
    print('-1')
    sys.exit()
i=1
K=9*K
ans=10-K

while(1):
    if 7*(ans-1)%K==0:
        print(i)
        sys.exit()
    i+=1
    ans=ans*10%K