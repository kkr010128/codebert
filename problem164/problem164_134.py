def Bfun():
    vals = [int(i) for i in input().split()]
    a = vals[0]
    b = vals[1]
    c = vals[2]
    d = vals[3]
    res2 = a//d + (1 if(a % d > 0) else 0)
    res1 = c//b + (1 if(c % b > 0) else 0)
    res = "Yes" if(res1 <= res2) else "No"
    print(res)
Bfun()