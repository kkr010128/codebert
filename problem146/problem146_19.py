"""
n = int(input())
ab = [list(map(int,input().split())) for _ in range(n)]

mod = 1000000007

ab1 = []
ab2 = []
ab3 = []
ab4 = []
count00 = 0
count01 = 0
count10 = 0

for i in range(n):
    if ab[i][0] != 0 and ab[i][1] != 0:
        ab1.append(ab[i][0]/ab[i][1])
        ab2.append(-ab[i][1]/ab[i][0])
        if ab[i][0]/ab[i][1] > 0:
            ab3.append((ab[i][0]/ab[i][1],-ab[i][1]/ab[i][0]))
        else:
            ab4.append((ab[i][0]/ab[i][1],-ab[i][1]/ab[i][0]))
    elif ab[i][0] == 0 and ab[i][1] == 0:
        count00 += 1
    elif ab[i][0] == 0 and ab[i][1] == 1:
        count01 += 1
    else:
        count10 += 1

dict1 = {}
dict2 = {}
ab3.sort()
ab4.sort(reverse = True)

print(ab3)
print(ab4)

for i in ab1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for i in ab2:
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1

sorted1 = sorted(dict1.items(), key = lambda x: x[0])
sorted2 = sorted(dict2.items(), key = lambda x: x[0])

print(sorted1)
print(sorted2)

cnt = 0
num1 = n - count00 - count01 - count10
ans = 0
for i in range(len(ab3)):
    a,b = ab3[i]
    num1 -= 1
    if cnt < len(sorted2):
        while cnt < len(sorted2):
            if sorted2[cnt][0] == a:
                ans += pow(2, num1+count01+count10-sorted2[cnt][1], mod)
                ans %= mod
                break
            elif sorted2[cnt][0] < a:
                cnt += 1
            else:
                ans += pow(2, num1+count01+count10, mod)
                ans %= mod
                break
        else:
            ans += pow(2, num1+count01+count10, mod) - pow(2, )
            ans %= mod
    print(ans)

for i in range(len(ab4)):
    num1 -= 1
    ans += pow(2, num1+count01+count10, mod)
    ans %= mod
    print(ans)

ans += pow(2, count01, mod) -1
print(ans)
ans += pow(2, count10, mod) -1
print(ans)
ans += count00
print(ans)

print(ans % mod)
"""

from math import gcd

n = int(input())

dict1 = {}
mod = 1000000007
cnt00 = 0
cnt01 = 0
cnt10 = 0

for _ in range(n):
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        cnt00 += 1
    elif a == 0:
        cnt01 += 1
    elif b == 0:
        cnt10 += 1
    else:
        c = gcd(a,b)
        if b < 0:
            a *= -1
            b *= -1
        set1 = (a//c, b//c)
        if set1 in dict1:
            dict1[set1] += 1
        else:
            dict1[set1] = 1

ans = 1

for k,v in dict1.items():
    a,b = k
    if dict1[(a,b)] == -1:
        continue
    if a > 0:
        if (-b,a) in dict1:
            ans *= 2**v + 2**dict1[(-b,a)] - 1
            dict1[(-b,a)] = -1
        else:
            ans *= 2**v
    else:
        if (b,-a) in dict1:
            ans *= 2**v + 2**dict1[(b,-a)] - 1
            dict1[(b,-a)] = -1
        else:
            ans *= 2**v
    ans %= mod

ans *= 2 ** cnt01 + 2 ** cnt10 - 1
ans += cnt00 - 1

print(ans%mod)
