def gcd(a,b):
    if a > b:
        x = a
        y = b
    else:
        x = b
        y = a
    while y > 0:
        r = x % y
        x = y
        y = r
    return x

def lcm(a,b,c):
    return int(a*b/c)

while 1:
    try:
        a,b = [int(x) for x in input().split()]
        res_gcd = gcd(a,b)
        res_lcm = lcm(a,b,res_gcd)
        print('{} {}'.format(res_gcd,res_lcm))
    except:
        break