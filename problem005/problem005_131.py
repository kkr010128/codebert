
while True:
    try:
        x = map(int, raw_input().split(' '))
        
        if x[0] < x[1]:
            m = x[1]
            n = x[0]
        else:
            m = x[0]
            n = x[1]
           
           
        # m is greatrer than n
        while n !=0:
            m,n = n,m % n
        
        print m,x[0]*x[1]/m
    except EOFError:
        break