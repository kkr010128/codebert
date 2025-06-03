def gcd(a,b):
    if(b==0):
        return a 
    return gcd(b,a%b)

while True:
    try:
        a,b = map(int, input().split())
        g = gcd(a,b)
        print("%s %d"%(g,a/g*b))
    except:
        break
