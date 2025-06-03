while True:
    n,x = list(map(int, input().split()))
    if n == 0 and x == 0:
        break
    res = 0
    i = 1
    while n-1 > i:
        j = i+1
        while n > j:
            k = j+1
            if x < i+k:
                break
            while n >= k:
                sum = i+j+k
                if sum == x:
                    res += 1
                elif x < sum:
                    break
                k += 1
            j += 1
        i += 1
    print(res)