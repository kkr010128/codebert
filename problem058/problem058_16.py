while True:
    n, x = map(int, input().split(" "))
    cnt = 0
    
    if n==x==0:
        break
    
    for i in range(1, n+1):
        for j in range (i+1, n+1):
            for k in range(j+1, n+1):
                if i+j+k==x:
                    cnt = cnt + 1
    
    print(str(cnt))