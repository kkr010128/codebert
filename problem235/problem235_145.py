import collections
import math
n = int(input())
ai = [int(i) for i in input().split()]

mod = 10**9+7

if n == 1:
    print(1)
    exit()
    
    
# 素因数分解、辞書で返すやつ
# mathをimportする
def prime(n):
    factor = {}
    tmp = int(math.sqrt(n)) + 1
    for num in range(2, tmp):
        while n % num == 0:
            n //= num
            if not num in factor.keys():
                factor[num] = 1
            else:
                factor[num] += 1
        if num > n:
            break
    if n != 1:
        if not n in factor.keys():
            factor[n] = 1
        else:
            factor[n] += 1
    return factor


dic = {}
for a in ai:
    pr = prime(a)
    for num, count in pr.items():
        if not num in dic.keys():
            dic[num] = count
        else:
            if dic[num] < count:
                dic[num] = count

kari = 1
for num,count in dic.items():
    kari *= pow(num,count,mod)
    kari %= mod

kari_old = kari
ans = 0

for i in range(n):
    kari = kari_old
    #com_ab_new = copy.deepcopy(com_ab)
    #print(com_ab,com_ab_new)
    #kari = 1
    #for j in range(kosu):
    #kari *= pow(sosu_li[j][0],com_ab[sosu_li[j][0]],mod)
    kari *= pow(ai[i],mod-2,mod)
    ans += kari
    ans %= mod
    #print(ans)
    #print(ans)
        
print(ans)
