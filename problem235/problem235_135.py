n = int(input())
a = list(map(int,input().split()))
di = 10**9+7
##試し割り
import math
import collections
def trial_division_prime(n, prime_list,prime_count):
    tmp=collections.Counter()
    for i in prime_list:
        if i * i > n:
            break
        while n % i == 0:
            n /= i
            tmp[i] += 1
    if n > 1:
        tmp[int(n)] += 1
    for num,rui in tmp.items():
        if prime_count[num]<rui:
            prime_count[num]=rui
        else:
            continue
    return prime_count
##ふるい
import itertools
def eratosthenes_sieve(n):
    table = [0] * (n + 1)
    prime_list = []

    for i in range(2, n + 1):
        if table[i] == 0:
            prime_list.append(i)
            for j in range(i + i, n + 1, i):
                table[j] = 1

    return prime_list

lis = eratosthenes_sieve(int(math.sqrt(max(a))+1))
prime_count = collections.Counter()
for i in a:
    cnt = trial_division_prime(i,lis,prime_count)
#print(cnt)
lcm=1
for s,t in prime_count.items():
    lcm=(lcm*pow(s,t,di))%di
#print(lcm)
su = 0
for i in a:
    div = pow(i,di-2,di)
    su = (su+(lcm*div)%di)%di
print(su)
