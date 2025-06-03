a,b,k = map(int,input().split())

if a == k :
    print(0,b)
elif a > k :
    print(a-k,b)
elif a < k :
    c = b - (k-a)
    if c >= 0 :
        print(0,c)
    else :
        print(0,0)
