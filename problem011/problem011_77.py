def gcd(a,b): 
    if b == 1:
        return 1
    else:
        return (gcd(b,a%b) if b != 0 else a)
A = list(map(int,input().split()))
print(gcd(A[0],A[1]))