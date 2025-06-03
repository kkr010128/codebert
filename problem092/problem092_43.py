X,k,d = map(int,input().split())
x = abs(X)

if x >= k*d:
    print(x - d*k)
else:
    e = x//d
    k -= e
    x %= d
    if k % 2 == 0:
        print(x)
    else:
        print(d-x)
