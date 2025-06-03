import math
A,B = map(int,input().split())

gcd = math.gcd(A,B)
d = []
if A == 1 or B == 1 :
    print(1)
    exit()
ans = [1]
while gcd %2 == 0 :
    gcd //= 2
    ans.append(2)
i = 3
while i * i <= gcd :
    if gcd %i == 0 :
        ans.append(i)
        gcd //= i
    else :
        i += 2
if gcd != 1 :
    ans.append(gcd)
print(len(set(ans)))
