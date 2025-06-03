#2-8
while True:
    try:

        def gcd(a,b):
            if b == 0:
                return a
            else:
                return gcd(b,a%b)

        a = list(map(int,input().split()))
        a.sort()
        a.reverse()
        ans1 = gcd(a[0],a[1])
        ans2 = int(a[0]*a[1]/ans1)

        print(ans1,ans2)
    except:
        break
