def GCD_calc(A,B):
    if(A>=B):
        big = A
        small = B
    else:
        big = B
        small = A
    r=big%small
    if r == 0:
        return small
    else:
        return GCD_calc(small,r)

a,b = map(int,input().split())
print(GCD_calc(a,b))

