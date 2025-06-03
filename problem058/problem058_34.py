

m = 0
while m == 0:
    n, x = map(int,raw_input().split())
    count = 0    
    if n == 0 and x == 0:
        break
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            for k in xrange(1,n+1):
                ans = i + j + k
                if ans == x and i != j and j != k and k != i:
                    count = count + 1
    print count / 6