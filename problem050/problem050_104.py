while True:
    H,W= map(int, input().split())
    if H==0 and W==0:
        break
    s = "#"
    a = H
    b = "."
    for i in range(H):
        if 1<a<H:
            y = s+b*(W-2)+s
            print(y)
            a-=1
        elif a==H or a==1:
            x = s*W
            print(x)
            a-=1                    
    print("")