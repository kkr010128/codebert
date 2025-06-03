while True:
    n,x = [int(x) for x in input().split()]
    if (n,x)==(0,0): break
    cnt=0
    if 3*(n-1) >= x:     # If n-2 + n-1 + n < x, there is no combination
        a_max = x//3 - 1 # a_max + a_max+1 + a_max+2 = x
        if 2*n-1 < x: 
            a_min = x - (2*n-1) # set minimum value of a
        else:
            a_min = 1
        for a in range(a_min,a_max+1):
            b_max = (x-a-1)//2 # b_max + b_max+1 <= x-a
            b_min = (x-a) - n  # set minimum value of b
            b_min = b_min if b_min > a+1 else a+1
            cnt += b_max - b_min + 1
    print(cnt)