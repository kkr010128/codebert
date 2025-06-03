import math
K = int(input())
result = 0
# 全て等しい場合はそれ自身が最大公約数
for i in range(1, K+1):
    result += i
# 二つが等しい場合は二つある方を選ぶので2倍、二数の公約数の三倍で6倍
d = {}
for i in range(1, K+1):
    for j in range(i+1, K+1):
        d[(i, j)] = math.gcd(i, j)
        result += 6 * d[(i, j)]
# 三つバラバラなら6倍
for i in range(1, K+1):
    for j in range(i+1, K+1):
        for k in range(j+1, K+1):
            tmp = 0
            if i < j:
                tmp = d[(i, j)]
            else:
                tmp = d[(j, i)]
            if tmp < k:
                result += 6 * d[(tmp, k)]
            else:
                result += 6 * d[(k, tmp)]
print(result)
