while True:
    a=int(input())
    if a==0 :
        break
    b=list(map(float,input().split()))
    m=sum(b)/a
    ver=0.0
    for i in b :
        ver+=(i-m)**2/a
        s=(ver)**0.5

    print(s)