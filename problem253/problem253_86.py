def main():
    n,a,b=map(int,input().split())
    di = 0
    if (b-a)%2==1:
        w = a-1
        l = n-b
        di = (w - l)
        if di < 0:
            di = -w-1
        else:
            di = l+1
        a += di
        if a < 1:
            a = 1
        b += di
        if b > n:
            b = n
    #print(a,b,di)
    print((b-a)//2 + abs(di))
    
if __name__ == "__main__":
    main()