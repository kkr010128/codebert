results = []
while True:

    n,x = map(int ,raw_input().split())
    
    if n is x is 0:
        break
    s = 0
    for i in xrange(1,n+1):
        for j in xrange(1,n+1):
            for k in xrange(1,n+1):
                if i+j+k == x:
                    if i != j and j != k and k != i :
                        s+=1
       
    results.append(s/6)

for i in results:
    print i