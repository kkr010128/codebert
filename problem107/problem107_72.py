def popcount(x):
    xb = bin(x)
    return xb.count("1")
def solve(x, count_1):
    temp = x %count_1
    if(temp == 0):
        return 1
    else:
        return 1 + solve(temp, popcount(temp))
n = int(input())
x = input()
x_b = int(x, 2)
mod = x.count("1")
xm1 = x_b %(mod+1)
if(mod != 1):
    xm2 = x_b %(mod-1)
for i in range(n):
    if(x[i] == "0"):
        mi = (((pow(2, n-1-i, mod+1) + xm1) % (mod+1)))
        if(mi == 0):
            print(1)
        else:
            print(1 + solve(mi, popcount(mi)))
    else:
        if(mod == 1):
            print(0)
        else:
            mi = ((xm2-pow(2, n-1-i, mod-1)) % (mod-1))
            if((x_b - xm2 == 0)):
                print(0)
            elif(mi == 0):
                print(1)
            else:
                print(1 + solve(mi, popcount(mi)))