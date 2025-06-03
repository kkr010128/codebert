n,a,b = map(int,input().split())

if (a+b) % 2 == 0:
    print(b - (a+b)//2)
else:
    if a <= n-b+1:
        b -= a
        print(a + b-(1+b)//2)
    else:
        a += n-b+1
        print(n-b+1 + n - (n+a)//2)

