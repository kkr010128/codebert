n = int(input())
x = int(input(),2)

def popcount(l):
    return bin(l).count("1")
def count(l):
    res = 0
    while l != 0:
        p = popcount(l)
        l %= p
        res += 1
    return res
m = popcount(x)
x_plus = x%(m+1)
if m != 1:
    x_minus = x%(m-1)
else:
    x_minus = 1
lis_plus = [0]*n
lis_minus = [0]*n
for i in range(n):
    if i == 0:
        lis_plus[i] = 1%(m+1)
        if m != 1:
            lis_minus[i] = 1%(m-1)
    else:
        lis_plus[i] = lis_plus[i-1]*2%(m+1)
        if m != 1:
            lis_minus[i] = lis_minus[i-1]*2%(m-1)
for i in range(n):
    if (x >> (n-i-1)) & 1:
        if m == 1:
            print(0)
        else:
            print(count((x_minus - lis_minus[-i-1])%(m-1)) + 1)
    else:
        print(count((x_plus + lis_plus[-i-1])%(m+1)) + 1)