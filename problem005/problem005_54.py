def gcd(li):
    a=max(li)
    b=min(li)
    while b>0:
        a,b=b,a%b
    return a

def lcm(li):
    return li[0]*li[1]/gcd(li)

while True:
    try:
        li=[int(i) for i in input().split(" ")]
        print("%i %i"%(gcd(li),lcm(li)))
    except:break