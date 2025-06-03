import math
import collections

n = int(input())
iwashi = []
sub_ans = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        sub_ans += 1
    else:
        if b == 0:
            iwashi.append('1/0')
        elif b > 0:
            c = math.gcd(a, b)
            iwashi.append('{}/{}'.format(a//c, b//c))
        else:
            c = math.gcd(a, b)
            iwashi.append('{}/{}'.format(-a//c, -b//c))
# print(iwashi)
iwashi = collections.Counter(iwashi)
k_list = list(iwashi.keys())
v = list(iwashi.values())
# k_list.sort(key=lambda x: -x)

mod = 1000000007
ans = 1
for k in k_list:
    a = iwashi[k]
    if k == '1/0':
        anti_k = '0/1'
    elif k == '0/1':
        anti_k = '1/0'
    else:
        c, d = k.split('/')
        if int(c) < 0:
            anti_k = '{}/{}'.format(d, -int(c))
        else:
            anti_k = '{}/{}'.format(-int(d), c)

    b = iwashi[anti_k]
    if a*b != 0:
        ans *= (pow(2, a, mod) + pow(2, b, mod) -1)
    else:
        ans *= pow(2, a, mod)
    iwashi[k] = 0
    iwashi[anti_k] = 0
    # print(k, anti_k ,a, b, ans)
    ans %= mod
print((ans+sub_ans-1)%mod)
