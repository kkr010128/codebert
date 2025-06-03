a, b, k = map(int, input().split())
if a==0 and b==0:
    print(0, 0)
elif k>a:
    if b-(k-a)>0:
        print(0, b-(k-a))
    else:
        print(0, 0)
elif k<a:
    print(a-k, b)
elif a==k:
    print(0, b)