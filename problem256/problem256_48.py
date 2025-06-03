def gcd(a,b):
    while True:
#         print(a,b)
        if a >= b:
            x = a
            y = b
        else:
            x = b
            y = a

        mod = x%y

        if mod == 0:
            return y
        
        else:
            a = y
            b = mod

A,B = list(map(int,input().split()))
ans = int(A*B / gcd(A,B))
print(ans)