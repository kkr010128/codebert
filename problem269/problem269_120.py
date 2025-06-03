def main():
    t1,t2=map(int,input().split())
    a1,a2=map(int,input().split())
    b1,b2=map(int,input().split())
    if a1<b1:
        a1,b1,a2,b2 = b1,a1,b2,a2

    d1 = a1*t1
    d2 = b1*t1

    dd1 = d1 - d2

    d1 += a2*t2
    d2 += b2*t2

    if d1 == d2:
        return "infinity"

    dd2 = d1 - d2

    if dd1 * dd2 > 0:
        return 0
    else:
        d1 += a1*t1
        d2 += b1*t1

        dd3 = d1 - d2

        if dd2 * dd3 > 0:
            return 1
        else:
            d1 += a2*t2
            d2 += b2*t2

            dd4 = d1 - d2
        if dd3 * dd4 > 0:
            return 2
        else:
            if dd1 > dd3:
                if dd1 % (dd1-dd3) == 0:
                    return (dd1 // (dd1-dd3) )*2
                else:
                    return (dd1 // (dd1-dd3) )*2+1
            else:
                if dd2 % (dd2-dd4) == 0:
                    return (dd2 // (dd2-dd4) )*2 +1
                else:
                    return (dd2 // (dd2-dd4) )*2+2



print(main())