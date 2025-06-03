while True:
    n,x = map(int,input().split())
    if n == x == 0:
        break
    
    d = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            k = x-(i+j)
            if k >= 1 and k<= n and k > j:
                d += 1
    
    print(d)
        
    
