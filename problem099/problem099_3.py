import math
N, K = map(int,input().split())
A = [int(i) for i in input().split()]

if K == 0:
    print(max(A))
else:
    low = 0
    high = max(A)
    while high - low > 0.1:
        mid = (low + high) / 2
        times = 0
        for a in A:
            times += math.ceil(a / mid) - 1
        if K >= times:
            high = mid
        else:
            low = mid
        #print(mid)

    ans = int(mid)
    if not ans:
        print(1)
    else:
        times = 0
        for a in A:
            times += math.ceil(a / ans) - 1
        if times <= K:
            print(ans)
        else:
            print(ans+1)
