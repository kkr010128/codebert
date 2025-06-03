while True:
    n,x = list(map(int, input().split()))
    if n == x == 0:
        break

    num_set = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i < j < k and i+j+k ==x:
                    li = [i,j,k]
                    if not li in num_set:
                        num_set.append(li)
    print(len(num_set))