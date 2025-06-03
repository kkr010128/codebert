N = int(input())
A = list(map(int,(input().split())))

sum=1

if 0 in A:
    print(0)
else:
    for i in range(N):
        sum *= A[i]  
        if sum >= int(1e18):
            break
    print(sum if sum<= int(1e18) else -1)