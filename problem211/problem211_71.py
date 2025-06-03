n,k=list(map(int,input().split()))
if(n>=10):
    print(int(k))
    
else:
    rating =k + 1000 - 100*n
    print(rating)