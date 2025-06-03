def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

while True:
    try:
        a,b=sorted(map(int,input().split()))
    except:
        break
    print(gcd(a,b),a//gcd(a,b)*b)