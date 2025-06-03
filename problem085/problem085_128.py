import math
n = int(input())
a = list(map(int, input().split()))
f = [0]*10**7
def fctr_d(n):
    c = 0
    r = int(n**0.5)
    for i in range(2, r+2):
        while n % i == 0:
            c += 1
            n = n//i
        if c != 0:
            if f[i] != 0:
                return False
            else:
                f[i] = True
                c = 0
    if n != 1:
        if f[n] != 0:
            return False
        else:
            f[n] = True
    return True


pairwise_flag = True
for i in range(n):
    m = a[i]
    if not fctr_d(m):
        pairwise_flag = False
        break

setwise_flag = True
gcd = a[0]
for i in range(1, n):
    gcd = math.gcd(gcd, a[i])
if gcd != 1:
    setwise_flag = False

if pairwise_flag:
    print("pairwise coprime")
else:
    if setwise_flag:
        print("setwise coprime")
    else:
        print("not coprime")



