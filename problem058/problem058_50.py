while True:
    count=0
    n,x = map(int,input().split())
    if n==x==0: break
    for a in range(n):
        for b in range(n):
            for c in range(n):
                if a<b<c and a+b+c==x-3:
                    count+=1
    print(count)