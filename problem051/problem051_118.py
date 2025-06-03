s = "#."
while True:
    H,W= map(int, input().split())
    if H==0 and W==0:
        break
    elif W%2==0 :
            w1=s*(W//2)
            w2="."+s*(W//2-1)+"#"
    elif W%2==1:
        w1=s*((W-1)//2)+"#"
        w2="."+s*((W-1)//2)


    for i in range(H):
        if i%2==0:
            print(w1)
        elif i%2==1:
            print(w2)

    print("")