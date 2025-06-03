
K=int(input())
i=0
if K%2==0 or K%5==0:
    print('-1')

else:
    for d in range(K):
        i=(10*i+7)%K
        if i==0:
            print(d+1)
            break
