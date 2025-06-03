a,b,c,k=map(int,input().split())
if a>=k:
    print(k)
elif (k>a) and (a+b>=k):
    print(a)
elif (a+b<k):
    print(a-(k-(a+b)))
    
