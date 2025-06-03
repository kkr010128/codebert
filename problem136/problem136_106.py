import collections

# 素因数分解の結果を返す
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

N = int(input())
res = collections.Counter(prime_factorize(N)) # Counter({2: 4, 3: 1})
keys = list(res.keys()) # [2, 3]
length = len(keys)
ans = 0

# 因数に関する処理
for i in range(length):
    num = keys[i] # 因数
    beki = res[num] # 因数numの個数
    temp = 1
    while(beki >= temp):
        beki -= temp
        ans += 1
        temp += 1
print(ans)