while True:
    try:
        n,x = map(int,raw_input().split())
        if n == x == 0:
            break
    except EOFError:
        break
    
    total = 0
    for k in range(1,n+1):
        for j in range(1,n+1):
            for l in range(1,n+1):
                if k!=j!=l and k + j + l == x and k<j<l:
                    total +=1
    print total                