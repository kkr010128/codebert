def gcd(aa,bb):
    while bb!=0:
        r=bb
        bb=aa%bb
        aa=r
    return aa
a,b=map(int,raw_input().strip().split())
#print a,b
print gcd(a,b)

